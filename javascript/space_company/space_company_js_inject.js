// JavaScript to auto-run the game "Space Company":
// https://sparticle999.github.io/SpaceCompany/

/*jslint devel*/        // allow console.log()
/*jslint white */       // allow odd whitespace
/*global $ */           // jQuery defines "$"

//
// TERMS OF ART:
//
//      Category:
//          the things at the top of the page (Resources, Solar System, ...)
//      Item:
//          the things down the left bar which appear when you click a Category
//          (Metal, Gems; Science production, Technologies; ...)
//          Called an Item b/c most of them are a physical good you possess
//      Page:
//          the things on the right side which appear when you click an Item
//          Named after the corresponding Item (Metal, Gems, ...)
//      Clack:
//          the things on each Page that allow you to purchase something
//          (Gain 1, Storage Upgrade, Miner, Heavy Drill ...)
//
// I will want to rename my functions and variables to match this list.

var tick_seconds = 1;

var DEBUG = false;
var DEBUG_tick = false;
var TEST = false;
var auto_request = false;
var auto_gain = false;

var prior_cick_time;

var pane_descriptors = {
    Interstellar:   "#interstellarTab_pane",
    // Machine:     "#machineTab",
    Nonexistent:    "#TestingOnly",
    Research:       "#research",
    Resources:      "#resources",
    "Sol Center":   "#solCenterPage",
    "Solar System": "#solarSystem",
    Stargaze:       "#stargazeTab_pane",
    Wonders:        "#wonder"
};

function from_number(value) {
    "use strict";
    var mult_idx = 0;
    while (value > 1000) {
        mult_idx += 1;
        value /= 1000;
    }
    value = Math.round(value * 1000) / 1000;    // round to 3 places
    var value_int = Math.round(value);
    if (value === value_int) {
        value = value_int;       // convert to type int if exact value
    }
    const multipliers = ["", "K", "M", "B", "T", "???"];
    var multiplier_str = multipliers[mult_idx];
    var answer = value.toString() + multiplier_str;
    return answer;
}

function to_number(orig_value) {
    "use strict";
    if (typeof orig_value !== 'string') {
        // console.log('to_number(): ignoring non-string', orig_value);
        return orig_value;
    }
    var value = orig_value;

    if (value === "Dormant") { return 0; }
    if (value === "Activated") { return 1; }

    if (value === "Not Built") { return 0; }
    if (value === "Built") { return 1; }

    if (value === "N/A") { return ""; }
    if (value === "n/a") { return ""; }

    value = value.replaceAll(",", "");
    value = value.replaceAll("/", "");   // Energy comes preceeded by "/" for some reason
    value = value.trim();                // and a million spaces
    if (value === "") {
        return "";
    }
    var answer = parseFloat(value);
    var multiplier_str = value.replace(/^-?[0-9.]*/, "");
    var multiplier = 1;
    switch(multiplier_str.toLowerCase()) {
        case "":    multiplier = 1;             break;  // 1 thousand
        case "k":   multiplier = 1000;          break;  // 1 thousand
        case "m":   multiplier = 1000000;       break;  // 1 million
        case "b":   multiplier = 1000000000;    break;  // 1 billion
        case "t":   multiplier = 1000000000000; break;  // 1 trillion
        default:
            throw new Error("to_number(): Invalid multiplier '" + multiplier_str + "' (" + orig_value + "->" + value + ") ");
    }
    // if (DEBUG) console.log("to_number:", value, multiplier_str, multiplier, answer);
    answer *= multiplier;
    answer = Math.round(answer);
    return answer;
}

function toHHMMSS(total_sec) {
    "use strict";
    if (total_sec === "INF") {
        return total_sec;
    }
    var days    = Math.floor(total_sec / 3600 / 24);
    var hours   = Math.floor(total_sec / 3600) % 24;
    var minutes = Math.floor(total_sec / 60) % 60;
    var seconds = Math.floor(total_sec % 60);

    days    = days.toString();
    hours   = hours.toString();   if (hours.length   < 2) { hours   = "0" + hours;   }
    minutes = minutes.toString(); if (minutes.length < 2) { minutes = "0" + minutes; }
    seconds = seconds.toString(); if (seconds.length < 2) { seconds = "0" + seconds; }

    var answers = [hours,minutes,seconds];

    var answer = "#" + days + "d " + answers.join(":").trim();

    answer = answer.replace("#0d ", "");
    answer = answer.replace("#", "");
    return answer;
}

function toElapsedTime(total_sec) {
    "use strict";
    if (total_sec === "INF") {
        return total_sec;
    }
    var days    = Math.floor(total_sec / 3600 / 24);
    var hours   = Math.floor(total_sec / 3600) % 24;
    var minutes = Math.floor(total_sec / 60) % 60;
    var seconds = Math.floor(total_sec % 60);

    if (days) { days += " days"; } else { days = ""; }
    if (hours) { hours += " hour"; } else { hours = ""; }
    if (minutes) { minutes += " min"; } else { minutes = ""; }
    if (seconds) { seconds += " sec"; } else { seconds = ""; }

    var answers = [days,hours,minutes,seconds];

    var answer = answers.join(" ").trim();
    if (answer === "") {
            answer = "0 sec";
    }
    return answer;
}

function sum(arr) {
    "use strict";
    return arr.reduce((a, b) => a + b, 0);
}

function jQuery_to_array(jquery_object) {
    "use strict";
    function filter_legal_item(line) {
        var index = line[0];
        if (index === "length") {
            return false;
        }
        if (index === "prevObject") {
            return false;
        }
        return true;
    }
    function map_second_value(line) {
        var item = line[1];
        return item;
    }
    var entries = Object.entries(jquery_object);
    var array = entries
        .filter(filter_legal_item)
        .map(map_second_value)
        ;
    return array;
}

function filter_not_empty(thing) {
    "use strict";
    return thing.length !== 0;
}

// some logic from Underscore UNIQUEID.JS:
var random_id_counter = 0;
function random_id(prefix) {
    "use strict";
    var id = "";
    random_id_counter += 1;
    id = random_id_counter + "";
    return prefix ? prefix + id : id;
}

function unused_random_id(prefix) {
    "use strict";
    var id = "";
    while (id === "") {
        id = random_id(prefix);
        if ( $( "#" + id ).length ) {
            // console.log("Skip used ID '" + id + "'");
            id = "";
        }
    }
    return id;
}

function uniqueId(ob, prefix) {
    "use strict";
    if (ob === "") {
        return "";
    }
    const ID = "id";
    // console.log('uniqueId(ob):', ob);
    var id = ob.attr(ID);
    if (id === undefined) {
        id = unused_random_id("uniq-" + prefix + '-');
        ob.attr(ID, id);
    }
    return id;
}

function add_class_remove_others(ob, className, classList) {
    "use strict";
    if (className) {
        ob.addClass(className);
    }

    classList.forEach(function(remove_me) {
        if (remove_me !== className) {
            ob.removeClass(remove_me);
        }
    });
}

function panesdesc_2_allowed(pane_descriptors, tabs_available) {
    "use strict";
    var pane_entries = Object.entries(pane_descriptors);

    var panes_allowed = pane_entries.filter(function(entry) {
        const [pane_heading, pane_desc] = entry;
        if (DEBUG) { console.log("debug: entry", entry, "values", pane_heading, pane_desc); }

        var available = tabs_available.includes(pane_heading);
        if (! available) {
            if (DEBUG) {console.warn("Skip unavailable tab", pane_heading);}
            return false;
        }
        return true;
    });

    return panes_allowed;
}

function panesdesc_2_left_trs(tabs_available) {
    "use strict";

    var panes_allowed = panesdesc_2_allowed(pane_descriptors, tabs_available);

    var available_panes = panes_allowed.map(function(entry) {
        const [pane_heading, pane_desc] = entry;
        // console.log("pane_heading, pane_desc", pane_heading, pane_desc);
        var tab = $( pane_desc + " > .container" );
        // console.log('tab', tab);
        var trs = tab
            .children("table")
            .children("tbody")
            .children("tr")
            ;
        trs = jQuery_to_array(trs);
        // console.log('trs', trs);
        var tr_obs = trs.map(function(tr) {
            return $( tr );
        });
        var trs_allowed = tr_obs.filter(function(tr) {
            var is_hidden = tr.hasClass('hidden');
            return (! is_hidden);
        });

        return [pane_heading, trs_allowed];
    });

    var leftbar = Object.fromEntries(available_panes);

    return leftbar;
}

function tr_to_tds(tr) {
    "use strict";
    tr = $( tr );
    var tr_id = uniqueId(tr, 'tr-left');
    var tds = tr.children('td');
    tds = jQuery_to_array(tds);
    return [tr_id, tds];
}

function td_to_spans(td) {
    "use strict";
    td = $( td );
    var spans = td.children('span');
    spans = jQuery_to_array(spans);
    return spans;
}

function cleanup_substance_name_simple(name) {
    "use strict";
    return name
        .trim()
        .toLowerCase()
        .replace("inside the ", "")
        .replace("the ","")
        .replace("comms", "communication")
        .replace("stargate", "stargate room")
        .replace("room room", "room")
        .replace("dyson swarms and sphere", "dyson segments")
        .replace("space rocket", "rocket")
        .replace(" production", "")
        .replace(": dormant", "")
        .replace(": activated", "")
        .replaceAll("-", "_")
        .replaceAll(" ", "_")
        ;
}

function cleanup_substance_name(name, pane_heading) {
    "use strict";
    name = name.trim();

    if (name === "Plasma") {
        if (pane_heading === "Sol Center") {
            // Disambiguate "Resource/Plasma" from "Sol Center/Plasma":
            name += " Unlock";
        }
    }

    return cleanup_substance_name_simple(name);
}

function textlist_2_substance(pane_heading, tr_id, texts) {
    "use strict";
    // if (pane_heading === "Sol Center") {
    //     console.warn('t2s(): Sol Center, texts=', texts);
    // }
    var substance = {};
    var A, B;
    switch (texts.length) {
    case 1:
        substance.name = texts[0];
        substance.count = "";
        // substance.rate = 0;
        // substance.max = "";
        break;
    case 2:
        substance.name = texts[0];
        substance.count = to_number(texts[1]);
        substance.rate = 0;
        substance.max = "";
        // if (pane_heading === "Sol Center") {
        //     console.warn('t2s(): Sol Center, substance=', substance);
        // }
        break;
    case 3:
        substance.name = texts[0];
        A = to_number(texts[1]);
        B = to_number(texts[2]);
        switch (substance.name) {
        case "Antimatter":
        case "Rocket Fuel":
        case "Science Production":
            substance.count = B;
            substance.rate = A;
            substance.max = "";
            break;
        case "Dark Matter":
            substance.count = A;
            substance.rate = 0;
            substance.max = A + B;
            break;
        case "Shield Plating":
        case "Engine Unit":
        case "Aerodynamic Sections":
            substance.count = A;
            substance.rate = 0;
            substance.max = B;
            break;
        default:
            console.error("T2S():", pane_heading, "3-element texts for invalid tab name '" + substance.name + "'", "texts", texts, "substance", substance);
            return null;
        }
        break;
    case 4:
        substance.name = texts[0];
        substance.rate = to_number(texts[1]);
        substance.count = to_number(texts[2]);
        substance.max = to_number(texts[3]);
        break;
    default:
        console.error('text list of invalid length', texts.length);
        return null;
        // break;
    }
    substance.pane = pane_heading;
    substance.tr_id = tr_id;
    if ((substance.name === "Space Rocket") && (substance.count === "")) {
        var rocket_count = $("#rocketRocketCost").text().trim();
        substance.count = to_number(rocket_count);
    }
    return substance;
}

function get_quantities(tabs_available) {
    "use strict";

    var leftbar = panesdesc_2_left_trs(tabs_available);

    var leftbar_entries = Object.entries(leftbar);

    var substance_list_all = leftbar_entries.map(function(entry) {
        const [pane_heading, trs] = entry;

        // DEBUG = (pane_heading === "Sol Center");

        if (DEBUG) {console.log('GQ(): pane_heading, trs', pane_heading, trs);}
        var tds_list = trs.map(function(tr) {
            var tds = tr_to_tds(tr);
            return tds;
        });
        if (DEBUG) {console.log('GQ() tds_list', tds_list);}

        var texts_list = tds_list.map(function(entry) {
            const [tr_id, td] = entry;
            if (DEBUG) {console.log('    gq(): tr_id', tr_id, 'td', td);}
            var spans = td_to_spans(td);
            var texts = spans.map(function(span) {
                span = $( span );
                var text = span
                    .text()
                    .trim()
                    .replace("/Sec", "")    // remove per-second from rate
                    .replaceAll("/", "")    // Energy comes preceeded by "/"
                    .trim()                 // and a million spaces
                    ;
                return text;
            }).filter(function(span) {
                // remove empty strings
                return span.length > 0;
            });
            return [tr_id, texts];
        }).filter(function(entry) {
            const texts = entry[1];
            // remove empty arrays
            return texts.length > 0;
        });

        var substance_list = texts_list.map(function(entry) {
            const [tr_id, texts] = entry;
            var substance = textlist_2_substance(pane_heading, tr_id, texts);
            // if (pane_heading === "Sol Center") {
            //     console.warn('GQ(): Sol Center, substance=', substance);
            // }
            return substance;
        });

        return substance_list;
    }).flat();

    // DEBUG = true;
    if (DEBUG) {console.log('GQ(): substance_list_all', substance_list_all);}
    // DEBUG = false;

    // pulling the counts from the Interstellar:Rockets page
    // TODO: Instead, we should wait and get this from the Clacks objects
    var plating_count = to_number($("#rocpart_shieldCount").text().trim());
    var engine_count = to_number($("#rocpart_engineCount").text().trim());
    var section_count = to_number($("#rocpart_aeroCount").text().trim());
    var fake_substances = [
        ["Shield Plating", plating_count, 50],
        ["Engine Unit", engine_count, 25],
        ["Aerodynamic Sections", section_count, 15]
    ];
    fake_substances.forEach(function(fake_item) {
        var new_substance = textlist_2_substance("Rocket Parts (fake)", "NONE", fake_item);
        substance_list_all.push( new_substance );
    });

    var quantities_list = substance_list_all.map(function(substance) {
        var name_clean = cleanup_substance_name(substance.name, substance.pane);
        return [name_clean, substance];
    });
    if (DEBUG) {console.log('GQ(): quantities_list', quantities_list);}

    var quantities = Object.fromEntries(quantities_list);
    // DEBUG = true;
    if (DEBUG) {console.log('GQ(): quantities', quantities);}
    // DEBUG = false;

    return quantities;
}

function check_energy_levels(quantities) {
    "use strict";

    // console.log('quantities:', quantities);
    var energy = quantities.energy;
    // console.log('energy:', energy);

    if (energy === undefined) {
        // energy doesn't exist yet
        return;
    }

    var energy_falling_case = (energy.rate <= 0);

    var energy_deficit_case = (energy.count === 0);

    var add_class;
    var all_energy_classes = [
        "energy-deficit",
        "energy-falling",
        "energy-okay"
    ];

    var game_ob = $("#game");
    if (energy_deficit_case) {
        add_class = "energy-deficit";
    } else if (energy_falling_case) {
        add_class = "energy-falling";
    } else {
        add_class = "energy-okay";
    }
    add_class_remove_others(game_ob, add_class, all_energy_classes);
}

var GLOBAL_known_missing_tabs = [];
function get_tabs_available() {
    "use strict";
    var answer = [];

    var tabList = $("#tabList li");
    $.each(tabList, function(index, value) {
        index = index;
        var ob = $( value );
        var hidden = ob.is(":hidden");
        if (hidden) {
            return;
        }
        var pull_right = ob.hasClass("pull-right");
        if (pull_right) {
            return;
        }
        var label = ob.text().trim();
        answer.push(label);

        var known_label = Object.keys(pane_descriptors).includes(label);
        if (! known_label) {
            if (! GLOBAL_known_missing_tabs.includes(label)) {
                console.log("VISIBLE TAB, UNKNOWN LABEL:", label);
                GLOBAL_known_missing_tabs.push(label);
            }
        }
    });

    return answer;
}

// fails gently if passed a non-object, and
// its output may always call .map or .filter:
function safeEntries(thing) {
    "use strict";
    if (thing === undefined) {
        return [];
    }
    return Object.entries(thing);
}

// creates an object whose keys are from column 1 and where *all* records
// from column 2 are joined into an array:
function arraysFromEntries(arr) {
    "use strict";
    var answer = {};
    arr.forEach(function(entry) {
        const [first, second] = entry;
        if (answer[first] === undefined) {
            answer[first] = [];
        }
        answer[first].push(second);
    });
    return answer;
}

function price_2_pair(price_str) {
    "use strict";
    if (price_str === "") {
        return [];
    }
    // console.log("price_str:", price_str)
    var price_split = price_str
        .replaceAll(" ", "_")       // any number of spaces -> underscore
        .replace("_", " ")          // first underscore -> space again
        .split(" ", 2);             // split on that first space
    // console.warn("price split:", price_split);
    const [neededC, substanceC] = price_split;
    var needed = to_number(neededC);
    var substance = substanceC.toLowerCase();
    if (substance === "gem") { substance = "gems"; }
    var price = [substance, needed];
    // console.log("price:", price);
    return price;
}

function prices_2_priceob(prices_str) {
    "use strict";
    // console.log('debug: prices_2_priceob(', prices_str, ')');
    var prices_list = prices_str
        .trim()
        .split(", ")    // split on "comma space"
        ;
    var prices_arr = prices_list.map(price_2_pair);
    var prices_ob = Object.fromEntries(prices_arr);
    return prices_ob;
}

function multiply_price(price_ob, multiplier) {
    "use strict";
    if (multiplier === 1) {
        return price_ob;
    }
    var price_entries = safeEntries(price_ob);
    var updated_price_entries = price_entries.map(function([substance, price]){
        return [substance, price * multiplier];
    });
    var updated_prices_ob = Object.fromEntries(updated_price_entries);
    return updated_prices_ob;
}

function panesdesc_2_panesob(pane_descriptors, tabs_available) {
    "use strict";
    var panes_allowed = panesdesc_2_allowed(pane_descriptors, tabs_available);
    // console.log("panes_allowed:", panes_allowed)

    var panes_array = panes_allowed.map(function(entry) {
        const [pane_heading, pane_desc] = entry;
        var panes = $( pane_desc + " .tab-pane");
        return [pane_heading, panes];
    });
    // console.log("panes_array:", panes_array)

    var panes_ob = Object.fromEntries(panes_array);
    return panes_ob;
}

function set_ob_title_by_string(ob, s) {
    "use strict";
    ob.prop("title", s);
    // console.log("Set ob title", s);
}

function set_ob_title_blank(ob) {
    "use strict";
    set_ob_title_by_string(ob, "");
}

function set_ob_title_by_array(ob, arr) {
    "use strict";
    if (arr.length) {
        var s = arr.join("\n");
        set_ob_title_by_string(ob, s);
    } else {
        set_ob_title_blank(ob);
    }
}

function get_button_raw(td) {
    "use strict";

    var button = td
        .find("button")
        [0];

    if (! button) {
        button = td
            .find("div.btn")
            [0];
    }

    if (! button) {
        return "";
    }

    button = $( button );

    return button;
}

function verify_button(button) {
    "use strict";

    if (button === "") {
        return "";
    }

    if (button.hasClass("destroy")) {
        console.error("destroy button!", button);
        return "";
    }

    if (button.hasClass("btn-warning")) {
        return "";
    }

    if (button.hasClass("disabled")) {
        return "";
    }

    var button_is_hidden = button
        .hasClass("hidden");

    if (button_is_hidden) {
        // console.log("button is hidden", button);
        return "";
    }

    button_is_hidden = button
        .parent()
        .hasClass("hidden");

    if (button_is_hidden) {
        // console.log("button parent is hidden", button.parent())
        return "";
    }

    return button;
}

function get_button(td, purchase) {
    "use strict";

    if (purchase === "Rocket Ship: Built") {
        // no button on already-built rocket ship
        return "";
    }

    if (purchase.includes("(MAX)")) {
        // console.log("found MAX:", purchase);
        return "";
    }

    var found = purchase.match(/:\ [0-9]+\/[0-9]+$/);
    if (found !== null) {
        found = purchase.match(/[0-9]+/g);
        if (found[0] === found[1]) {
            // e.g. "25/25"
            return "";
        }
    }

    var button = get_button_raw(td);
    button = verify_button(button);

    return button;
}

function inputid_2_desired(input_id) {
    "use strict";
    var desired = "";
    if (input_id) {
        var val = $("#" + input_id).val();
        if (val) {
            desired = val.trim();
            if (desired < 0) {
                // don't allow negative values
                desired = "";
            }
        }
    }
    return to_number(desired);
}

function create_input_and_get_id(button_id, debug_label) {
    "use strict";

    if (button_id === "") {
        // no button: don't create an input
        return "";
    }

    var desired_class = "desired";
    var input_class = button_id;    // yes, using button_id as a class here

    var input = $("." + desired_class + "." + input_class);
    if (input.length === 0) {
        // "input" not found
        if (! button_id) {
            // no button or input --> okay
            return;
        }
        // button but no input: create input
        // console.log(debug_label, "Creating input object:");
        input = $("<input type='textbox' class='" + desired_class + "'/>");
        var button_ob = $("#" + button_id);
        button_ob.after(input);
    } else {
        // "input" is found
        if (! button_id) {
            // input but no button: input is obsolete
            console.warn(debug_label, "Destroying input object:");
            input.remove();
        // } else {
        //     // both button and input: okay
        }
    }
    input.addClass(input_class);

    return uniqueId(input, 'input');
}

function create_display_and_get_id(button_id, debug_label) {
    "use strict";

    if (button_id === "") {
        // no button: don't create a display
        return "";
    }

    var display_class = "display";
    var span_class = button_id;    // yes, using button_id as a class here

    var display = $("." + display_class + "." + span_class);
    if (display.length === 0) {
        // "display" not found
        if (! button_id) {
            // no button or input --> okay
            return;
        }
        // button but no display: create display
        console.log(debug_label, "Creating display object:");
        display = $("<span class='" + display_class + "'>SET ME</span>");
        var button_ob = $("#" + button_id);
        button_ob.after(display);
    } else {
        // "display" is found
        if (! button_id) {
            // display but no button: display is obsolete
            console.warn(debug_label, "Destroying display object:");
            display.remove();
        // } else {
        //     // both button and display: okay
        }
    }
    display.addClass(span_class);

    return uniqueId(display, 'display');
}

var GLOBAL_known_unknowns = [];
function complain_about_unknown_substances_once(unknown_substances_list) {
    "use strict";
    if (! unknown_substances_list) {
        return;
    }
    var answers = unknown_substances_list.map(function(substance) {
        var seen = (GLOBAL_known_unknowns.includes(substance));
        if (! seen) {
            GLOBAL_known_unknowns.push(substance);
            return true;
        }
        return false;
    });
    if (DEBUG) { console.log('DEBUG: complain answers', answers); }
    return;
}

function get_unknown_substances(prices_ob, quantities) {
    "use strict";

    var prices_list = safeEntries(prices_ob);

    var known_substances_list = Object.keys(quantities);
    // console.log('known_substances_list:', known_substances_list);

    var unknown_substances_list = prices_list.filter(function(entry) {
        const substance = entry[0];
        // console.log('substance:', substance);
        var known_substance = known_substances_list.includes(substance);
        return (! known_substance);
    });
    if (unknown_substances_list.length > 0) {
        var unknown_substances_ob = Object.fromEntries(unknown_substances_list);
        return unknown_substances_ob;
    } else {
        return "";
    }
}

function get_bump_max_ob(costs_ob, quantities) {
    "use strict";
    var costs_list = Object.entries(costs_ob);

    var bump_max_list = costs_list.filter(function([substance, needed]) {
        var item_ob = quantities[substance];
        if (item_ob === undefined) {
            // no such substance: problem
            return true;
        }
        var max_value = item_ob.max;
        if (max_value === "") {
            // no max -> no problem
            return false;
        }
        return (needed > max_value);
    });
    if (bump_max_list.length > 0) {
        var bump_max_ob = Object.fromEntries(bump_max_list);
        return bump_max_ob;
    } else {
        return "";
    }
}

function get_high_cost_and_time_ob(costs_ob, quantities) {
    "use strict";
    var costs_list = Object.entries(costs_ob);

    var high_cost_and_time_list = costs_list.map(function([substance, needed]) {
        var item_ob = quantities[substance];
        if (item_ob === undefined) {
            // no such substance: ignore
            return null;
        }
        var item_count = item_ob.count;
        var item_rate = item_ob.rate;
        if (item_count === "") {
            console.log('DEBUG: checking high cost for non-counted substance', substance, 'needed', needed, 'count', item_count);
            // no count: ignore
            return null;
        }
        var remaining = needed - item_count;
        if (remaining <= 0) {
            // have enough already: ignore
            return null;
        }

        var time_left;
        if (item_rate <= 0) {
            time_left = "INF";
        } else {
            time_left = remaining / item_rate;
        }

        return [substance, needed, time_left];
    }).filter(function(entry) {
        return entry !== null;
    });

    if (high_cost_and_time_list.length > 0) {
        var high_cost_list = high_cost_and_time_list.map(
            function(entry) {
                // label and column 1
                return [ entry[0], entry[1] ];
            }
        );
        var time_list = high_cost_and_time_list.map(
            function(entry) {
                // label and column 2
                return [ entry[0], entry[2] ];
            }
        );
        var high_cost_ob = Object.fromEntries(high_cost_list);
        var time_ob = Object.fromEntries(time_list);
        return [high_cost_ob, time_ob];
    } else {
        return ["", ""];
    }
}

function get_high_rate_ob(rates_ob, quantities) {
    "use strict";
    if (rates_ob === "Need not found") {
        console.error('debug: rates_ob', rates_ob);
        return "";
    }
    var rate_list = Object.entries(rates_ob);

    var high_rate_list = rate_list.filter(function([substance, needed]) {
        var item_ob = quantities[substance];
        if (item_ob === undefined) {
            // no such substance: problem
            return true;
        }
        var rate_value = item_ob.rate;
        if (rate_value === "") {
            console.log('DEBUG: checking high rate for non-counted substance', substance, 'needed', needed, 'count', rate_value);
            // no rate -> no problem
            return false;
        }
        return (needed > rate_value);
    });
    if (high_rate_list.length > 0) {
        var high_rate_ob = Object.fromEntries(high_rate_list);
        return high_rate_ob;
    } else {
        return "";
    }
}

function details_2_cost_need_make(orig_details, pane_title, purchase, clean_name) {
    "use strict";

    // create cost_need_make object and set failure defaults:
    var c_n_m = {
        cost: "Cost not found",
        need: "Need not found",
        make: "Make not found",
        details_orig: "SET ME",
        details: "SET ME"
    };

    var details = orig_details
        .replaceAll("\n", " ")
        .replaceAll("\t", " ")
        .replaceAll(/\ \ +/g, " ")
        .replaceAll("{", "(")
        .replaceAll("}", ")")
        .replaceAll(":", " -- ")
        ;

    var replacements = {
        "---": [
            /\ [0-9.]+%/g,          // " 99.5%"
            /\[.*\]/g,              // "[3d 23:59:59]"
            /Activate\ .*\ Wonder/g,
            /Rebuild\ .*\ Wonder/g,
            "Activate Portal",
            "Donate Resources",
            "Unlock Dyson Sphere Research",
            "Unlock EMC Machine Research",
            "Unlock Plasma Research",

            // misuse of "uses" or "produces":
            "produces a lot of power",
            "produces Gems at intense speeds",
            "Uses fission to create large amounts of power",
            "uses nano-fibres",

            // misuse of " for ":
            "allow for easy",
            "allow for enough",
            "allows for a massive increase",
            "asteroids for gold",
            "axe for your woodcutter",
            "batteries for all",
            "blueprints for this",
            "designed for mining",
            "field for pieces",
            "for this knowledge",       // NOTE: also in "}" section
            "game for tools",
            "machines, for powerful",
            "machines, for propulsion",
            "makes up for in",
            "necessary for Tier",
            "need for fuel",
            "pickaxe for your miner",
            "power for your",
            "return for building",
            "return for your",
            "search for Titanium",
            "science) for each Dark Matter",
            "shovel for your woodburner",
            "source for your",
            "store it for later use",
            "upgrade for dark matter",
            "Uranium for easy",
            "used for advanced",
            "used for building",
            "used for many",
            "used for nuclear",
            "used for super-cooling",
            "useful for automatic",
            "useful for inter-star-system",
            "Wonders, for complex",

            // misuse of "out of":
            "landings out of atmospheres",
            "transportation out of deep",

            "ZZZ LAST NO COMMA"
        ],
        "}{COST:": [
            "Costs:",
            "Costs -- ",    // we've replaced colons with em-dashes above ...
            "costs -- ",    // ...
            "Costs ",
            "Cost:",
            "Cost -- ",     // ... so this is what really matches now
            "Cost ",
            "created by infusing",
            "He requests a pyramid containing",
            "He requests a tower consisting of",
            "He requires that you donate",
            "However, it requires",
            "It requires",
            "out of",
            "The Overlord wishes for a cube made up of",
            "This requires",

            "ZZZ LAST NO COMMA"
        ],
        "}{MAKE:": [
            "it can produce",
            "It will produce",
            "it will produce",
            "Produces",
            "produces",
            ", produces ",
            "that can produce",
            "They produce",

            "ZZZ LAST NO COMMA"
        ],
        "}{NEED:": [
            "They use",
            "Uses",
            ", uses ",

            "ZZZ LAST NO COMMA"
        ],
        "}{OTHER:": [
            " for ",            // close SOMETHING, open INVERSE

            "ZZZ LAST NO COMMA"
        ],
        "}": [
            /$/g,
            ". ",
            "each second",
            "every second",
            "for this knowledge",           // NOTE: also in "misuse of for" section
            "Improves relationship by",
            "in total",
            "per second",
            "to acquire his methods",
            "to assemble the",
            "to be given this technology",
            "to build the",
            "to create the",
            "to unlock this technology",

            "ZZZ LAST NO COMMA"
        ],
        ZZZ: ["ZZZ LAST NO COMMA"]
    };

    // things which have neither a Need nor a Make section:
    const purchase_ignore_both = [
        "Basic Energy Production",
        "Batteries",
        "Plasma Storage Units",
        'PSUs',
        "Storage Upgrade",
        "Storage Upgrades",
        // -----
        "Battery Efficiency",
        "Energy Efficiency",
        "Resource Efficiency",
        "Science Efficiency",
        // -----
        "Research",
        "Activate Portal",
        "Activate Wonder",
        "Energetic Wonder",
        "Meteorite Wonder",
        "Precious Metals Wonder",
        "Rebuild Antimatter Wonder",
        "Rebuild Communication Wonder",
        "Rebuild Rocket Wonder",
        "Rebuild Stargate Wonder",
        "Technological Wonder",
        // -----
        "Astronomical Breakthrough",
        "Dyson Segment",
        "Interstellar Radar Scanner",
        "Rocket Ship: Not Built",
        "Rocket Ship: Built",
        "Aerodynamic Sections",
        "Engine Unit",
        "Shield Plating",
        "Rebirth",
        "Respec",
        // -----
        "ZZZ LAST NO COMMA"
    ];

    const purchase_ignore_need = [
        "Empowered Blowtorch",
        "Explorer",
        "Gem Miner",
        "Grinder",
        "Heat Resistant Crucible",
        "Helium Drone",
        "Hydrogen Collector",
        "Ice Pickaxe",
        "Miner",
        "Native Moon Worker",
        "Rocket Droid",
        "Scout Ship",
        "Small Pump",
        "Solar Panels",
        "Vacuum Cleaner",
        "Woodcutter",
        // -----
        "Dyson Ring",
        "Dyson Swarm",
        "Dyson Sphere",
        // -----
        "ZZZ LAST NO COMMA"
    ];

    const purchase_ignore_make = [
        // "none yet",
    ];

    const pane_ignore_both = [
        "dark_matter",
        "rocket",
        "technologies",
        // -----
        "moon",
        "venus",
        "mars",
        "asteroid_belt",
        "wonder_station",
        "jupiter",
        "saturn",
        "pluto",
        "kuiper_belt",
        "sol_scientific_center",
        "military",
        // -----
        "carnelian_resistance",
        "prasnian_empire",
        "hyacinite_congregation",
        "kitrinos_corporation",
        "moviton_syndicate",
        // -----
        "ZZZ LAST NO COMMA"
    ];

    const pane_ignore_need = [
        "science",
        "ZZZ LAST NO COMMA"
    ];

    const pane_ignore_make = [
        // none yet
    ];

    // set success defaults for each Page or Clack that doesn't need a data type:
    if (pane_title === "energy_mass_conversion") {
        if (purchase !== "Research") {
            // does not have Costs section
            c_n_m.cost = "";
        }
    }

    if (purchase === "Rocket Ship: Built") {
        // does not have Costs section anymore after being built
        c_n_m.cost = "";
    }

    if (pane_title === "travel") {
        // Interstellar.
        // does not have Costs section
        c_n_m.cost = "";
    }

    if (details === "") {
        // details is now blank: return nothing
        c_n_m.cost = "";
        c_n_m.need = "";
        c_n_m.make = "";
    }

    if (purchase.includes("gain_")) {
        c_n_m.cost = "";    // some, e.g. Plasma, do have a cost; if so, that overrides this
        c_n_m.need = "";
        c_n_m.make = "";
    }

    // ignore, by "purchase"
    if (purchase_ignore_need.includes(clean_name)) {
        c_n_m.need = "";
    }

    if (purchase_ignore_both.includes(clean_name)) {
        c_n_m.need = "";
        c_n_m.make = "";
    }

    if (purchase_ignore_make.includes(clean_name)) {
        c_n_m.make = "";
    }

    // ignore, by "pane"
    if (pane_ignore_need.includes(pane_title)) {
        c_n_m.need = "";
    }

    if (pane_ignore_both.includes(pane_title)) {
        c_n_m.need = "";
        c_n_m.make = "";
    }

    if (pane_ignore_make.includes(pane_title)) {
        c_n_m.make = "";
    }

    details = details.replaceAll(" and ", ", ");
    details = details.replaceAll(" with ", ", ");

    // search for begin/end of each data type:
    safeEntries(replacements).forEach(function([new_string, target_list]) {
        target_list.forEach(function(target_string) {
            details = details.replaceAll(target_string, new_string);
        });
    });

    // clean up data
    details = details
        .replaceAll(/[\-\ .]+[}]/g, "}")    // dashes, spaces, or periods before a close-bracket
        .replaceAll(/[}][}]+/g, "}")        // two close-brackets become one
        ;
    const JUNK = "JUNK:";
    details = JUNK + details;
    var sections = details
        .split("{")
        .filter(filter_not_empty)
        ;
    // console.log('sections:', sections);
    var cleaned = sections.map(
        function(section){
            var fragments = section
                .split("}")
                .filter(filter_not_empty)
                ;
            if (fragments.length > 1) {
                fragments = fragments.map(function(frag, idx) {
                    if (idx === 0) {
                        return frag.trim();
                    }
                    // console.warn('extra junk section', details, fragments, frag);
                    return JUNK + frag;
                });
            }
            return fragments;
        })
        .flat()
        .filter(filter_not_empty)
        ;

    var answers = cleaned.map(function(section) {
        var pieces = section.split(":");
        if (pieces.length > 2) {
            // shouldn't be possible, since we've replaced colons with em-dashes above
            console.error('pieces > 2', pieces);
            throw new Error('D2c_n_m(): found extra colon in a section');
        }
        return pieces;
    });
    // console.log('orig_details:', orig_details);
    // console.log('details:', details);
    // console.log('answers:', answers);

    var answers_lowercase = answers.map(function([label, data]) {
        return [label.toLowerCase(), data];
    });
    var c_n_m_entries = arraysFromEntries(answers_lowercase);
    // console.log('c_n_m_entries [A]:', c_n_m_entries);

    var c_n_m_keys = Object.keys(c_n_m_entries);
    var prior_key = "";
    c_n_m_keys.forEach(function(key) {
        var value_arr = c_n_m_entries[key];
        var value_str = value_arr
            .map(function(s) { return s.trim(); })
            .join(", ")   // must match prices_2_priceob!
            ;
        if (key === "other") {
            if (prior_key === "") {
                console.error('got an OTHER without a PRIOR!');
                console.warn('key:', key, 'value_str:', value_str);
                console.log('answers:', answers);
                console.log('details:', details);
            } else if (prior_key === "make") {
                key = "need";
            } else if (prior_key === "need") {
                key = "make";
            } else {
                console.error('got an OTHER with an INVALID PRIOR:', prior_key);
                console.warn('key:', key, 'value_str:', value_str);
                console.log('answers:', answers);
                console.log('details:', details);
            }
        }
        if ((key === "make") || (key === "need")) {
            prior_key = key;
        }
        if (key === "junk") {
            c_n_m[key] = value_str;
        } else {
            try {
                c_n_m[key] = prices_2_priceob(value_str);
            } catch (e_const) {
                var e = e_const;
                if (!(e instanceof Error)) {
                    e = new Error(e);
                }
                console.error(e.message);
                console.warn('key:', key, 'value_str:', value_str);
                console.log('answers:', answers);
                console.log('details:', details);
            }
        }
    });
    // console.log('c_n_m_entries [B]:', c_n_m_entries);

    // XYZZY

    c_n_m.details = details;

    var make = c_n_m.make;
    if (make === "") {
        make = {};
    }
    var make_entries = Object.entries(make);
    var make_entry;

    switch(make_entries.length) {
      case 0:
        c_n_m.make_item = "";
        c_n_m.make_count = 0;
        break;
      case 1:
        make_entry = make_entries[0];
        c_n_m.make_item = make_entry[0];
        c_n_m.make_count = make_entry[1];
        break;
      default:
        c_n_m.make_item = "ERROR: make.length > 1";
        c_n_m.make_count = make_entries.length;
    }

    return c_n_m;
}

function set_display_value(display_id, value) {
    "use strict";
    if (display_id) {
        var display = $('#' + display_id);
        if (value) {
            // NOTE: this bracket MUST be here, to separate this from the Costs section:
            value = "[" + value + "]";
        }
        display.text(value);
    }
}

function compose_clack_object(pane_title, purchase, details, current_ob, button_ob, tr_id, clack_type) {
    "use strict";
    var clack = {};
    clack.name = purchase;
    clack.type = clack_type;

    var clean_name = purchase
        .replace(' / ', '')
        .replace(/\ \(MAX\)$/, '')
        .replace(new RegExp("/[0-9]*$"), "")    // remove "/NN" from end
        .replace(new RegExp(": [0-9]*$"), "")   // remove ": NN" from end
        .replace(/[#0-9]+$/, "")                // remove "#N" or "NN" from end
        .replace(/^Tier\ [0-9]+\ /, '')
        .replace(/^T[0-9]+\ /, '')
        .replace(/#$/, '')
        .trim();
    clack.clean_name = clean_name;

    clack.pane_title = pane_title;

    if (clack.name === "Exploration") {
        var explore_where = ":" + clack.pane_title;
        clack.name += explore_where;
        purchase = clack.name;
        clack.clean_name += explore_where;
    }

    var current;
    if (current_ob === "") {
        current = "0";
    } else {
        current = current_ob
            .text()
            .trim();
    }
    clack.current = to_number(current);

    var button_id = uniqueId(button_ob, 'btn');
    clack.button_id = button_id;
    var button_text = "";
    var multiplier = 1;

    if (button_ob !== "") {
        button_text = button_ob.text().trim();
        clack.button_text_DEBUG = button_text;
        if (clack_type === "gain") {
            if (button_text.includes("20")) {
                multiplier = 20;
                clack.button_multiplier_DEBUG = multiplier;
            }
        }
    }
    var input_id = create_input_and_get_id(button_id, pane_title + "/" + purchase);
    clack.input_id = input_id;

    clack.desired = inputid_2_desired(input_id);
    clack.click_requested = ((clack.desired > 0) ? 1 : 0);

    var display_id = create_display_and_get_id(button_id, pane_title + "/" + purchase);
    clack.display_id = display_id;

    clack.details = details;

    var cost_need_make = details_2_cost_need_make(details, pane_title, purchase, clean_name);

    clack.cost = multiply_price(cost_need_make.cost, multiplier);
    clack.need = cost_need_make.need;
    clack.make = cost_need_make.make;
    clack.make_item = cost_need_make.make_item;
    clack.make_count = cost_need_make.make_count;
    clack.junk = cost_need_make.junk;

    clack.details = cost_need_make.details;

    clack.tr_id = tr_id;

    return clack;
}

/*
    clack = {
        // Set by tr_2_clack_raw():

        "name": "Storage Upgrade #12/25",
        "clean_name": "Storage Upgrade",
        "pane_title": "Metal"

        "current": 0,
        "desired": 25,        // == actually "how many MORE should we get"
        "click_requested": 1, // == 1 if desired > 0

        "button_id": "uniq-btn-28",
        "input_id": "uniq-input-99",

        "desired": 12,
        "click_requested": 1,

        "cost": "" | {list of substances with count},

        "need": "" | {list of substances with count},

        "make": "" | {list of substances with count},
        "make_item": "energy",
        "make_count": 1,

        "details": "description including Costs, Make, and Need",

        "tr_id": "heliumStorageUpgrade",

        // ----------------------------------------------------------------

        // Set by update_clack_fields():

        "unknown": [list of substances],
        "bump_max": "" | {list of substances with count},
        "high_cost": "" | {list of substances with count},
        "high_rate": "" | {list of substances with count},

        "clickable": "no_button|unknown|bump_max|high_rate|high_cost|OK",

        "type": "normal|gain|storage|dyson",    // TODO: should add some types here

        "details": << usually deleted >>
    };
*/

function create_dyson_clack(pane_title, dyson_product, dyson_subpage, details_end_str, dyson_current_id, dyson_max_id, dyson_button_ob) {
    "use strict";
    dyson_subpage = $( dyson_subpage );
    var dyson_tr_id = uniqueId(dyson_subpage);
    var dyson_details = dyson_subpage
        .text()
        .trim()
        ;

    if (details_end_str !== "") {
        var position = dyson_details.search(details_end_str);
        if (position === -1) {
            throw new Error("dyson_segments: Invalid dyson_details (should contain '" + details_end_str + "'): " + dyson_details);
        }
        dyson_details = dyson_details.slice(0, position);
    }

    var dyson_current_ob = $( dyson_current_id );
    dyson_button_ob = $( dyson_button_ob );

    if (dyson_max_id !== "") {
        var dyson_max_ob = $( dyson_max_id );
        var dyson_current_val = to_number(dyson_current_ob.text().trim());
        var dyson_max_val = to_number(dyson_max_ob.text().trim());
        if (dyson_current_val >= dyson_max_val) {
            // console.warn('dyson sphere counts: compare', dyson_current_val, dyson_max_val, 'MAX REACHED');
            dyson_button_ob = "";
            dyson_product += " (MAX)";
        }
    }

    // console.warn('compose_clack_object()', pane_title, dyson_product, dyson_details, dyson_current_ob, dyson_button_ob, dyson_tr_id, "dyson");
    var dyson_clack = compose_clack_object(pane_title, dyson_product, dyson_details, dyson_current_ob, dyson_button_ob, dyson_tr_id, "dyson");
    // console.warn('compose_clack_object()', dyson_clack);

    return dyson_clack;
}

function tr_2_clack_raw(tr, pane_title) {
    "use strict";
    var button_ob;
    var clack;
    var clack_type = "normal";      // should depend on pane_title

    // if (pane_title === "technologies") {
    //     clack_type = "science";
    // }

    tr = $( tr );
    // TODO: this once threw an error:
    // Uncaught TypeError: can't assign to property "id" on -1.8359385912006677e+289: not an object
    // I have no idea how the $() fn returned a number ?!?
    var tr_id = uniqueId(tr, 'tr-right');

    var details = tr
        .find("td > span")
        .text()
        .trim()
        ;

    var td = tr.find("td");

    var h3 = tr.find("h3");
    var purchase = h3
        .text()
        .trim()
        ;

    if (! purchase) {
        // no H3 value: either HR#0, or an invalid HR.
        button_ob = td.find("hide.gainButton > div.btn-default");
        if (button_ob.length === 0) {
            return null;
        }
        purchase = "gain_" + pane_title;
        clack = compose_clack_object(pane_title, purchase, details, "", button_ob, tr_id, "gain");
        return clack;
    }
    var is_hidden = tr.hasClass("hidden");
    if (is_hidden) {
        /* if (DEBUG) */ console.warn(pane_title, purchase, "HIDDEN");
        return null;
    }
    if (pane_title === "energy_mass_conversion") {
        if (purchase !== "Research") {
            return null;
        }
    }
    if (pane_title === "dyson_segments") {
        if (purchase !== "Research") {
            // this is where we wire in the special Dyson Sphere code

            var dyson_page = tr.find('td').find('> span');
            var dyson_buttons = dyson_page.find('button');
            var dyson_spans = dyson_page.find('span').not('.display');

            if (dyson_buttons.length !== 10) {
                console.error('THROWING ERROR');
                console.error("dyson_buttons", dyson_buttons.length + ")", dyson_buttons);
                throw new Error("dyson_segments: Invalid dyson_buttons.length (should be 10)");
            }
            if (dyson_spans.length !== 19) {
                console.error('THROWING ERROR');
                console.error("dyson_spans", dyson_spans.length + ")" , dyson_spans);
                throw new Error("dyson_segments: Invalid dyson_spans.length (should be 19)");
            }

            var dyson_objects = [];

            //////////////////////////
            // Construction clack:  //
            //////////////////////////

            dyson_objects.push(
                create_dyson_clack(
                    pane_title,
                    "Dyson Segment",
                    dyson_page,
                    "Build Dyson Segment",
                    "#dysonPieces2",
                    "",
                    dyson_buttons[0]
                )
            );

            //////////////////////////
            // Ring clack:          //
            //////////////////////////

            dyson_objects.push(
                create_dyson_clack(pane_title,
                    "Dyson Ring",
                    dyson_spans[6],
                    "",
                    "#ring",
                    "",
                    dyson_buttons[4]
                )
            );

            //////////////////////////
            // Swarm clack:         //
            //////////////////////////

            dyson_objects.push(
                create_dyson_clack(
                    pane_title,
                    "Dyson Swarm",
                    dyson_spans[10],
                    "",
                    "#swarm",
                    "",
                    dyson_buttons[6]
                )
            );

            //////////////////////////
            // Sphere clack:        //
            //////////////////////////

            dyson_objects.push(
                create_dyson_clack(
                    pane_title,
                    "Dyson Sphere",
                    dyson_spans[15],
                    "",
                    "#sphere",
                    "#sphereMax",
                    dyson_buttons[8]
                )
            );

            // console.warn('dyson_objects', dyson_objects);

            return dyson_objects;
        }
    }

    var current_ob = h3
        .find("span");

    button_ob = get_button(td, purchase);

    if (purchase === "Storage Upgrade") {
        clack_type = "storage";
    }

    clack = compose_clack_object(pane_title, purchase, details, current_ob, button_ob, tr_id, clack_type);

    return clack;
}

function update_clack_fields(clack, pane_title, quantities) {
    "use strict";

    if (clack === null) {
        return clack;
    }

    // console.log('quantities:', quantities);

    var unknown_substances_list = [
        get_unknown_substances(clack.need, quantities),
        get_unknown_substances(clack.make, quantities),
        get_unknown_substances(clack.cost, quantities)
    ];

    // console.log('unknown_substances_list:', unknown_substances_list);

    var unknown_substances_entry_list = unknown_substances_list.map(function(unknown_ob) {
        return safeEntries(unknown_ob);
    }).flat();

    var unknown_substances_ob = Object.fromEntries(unknown_substances_entry_list);
    // console.warn('unknown_substances_ob:', unknown_substances_ob);
    var unknown_substances = Object.keys(unknown_substances_ob);

    complain_about_unknown_substances_once(unknown_substances);
    if (unknown_substances.length) {
        if (DEBUG) { console.warn("cost of UNKNOWN SUBSTANCES:", pane_title, clack.name, unknown_substances); }
    } else {
        unknown_substances_ob = "";
    }
    clack.unknown = unknown_substances_ob;

    clack.bump_max = get_bump_max_ob(clack.cost, quantities);

    var high_cost_and_time = get_high_cost_and_time_ob(clack.cost, quantities);
    const [high_cost, high_cost_time] = high_cost_and_time;
    clack.high_cost = high_cost;
    clack.high_cost_time = high_cost_time;

    clack.high_rate = get_high_rate_ob(clack.need, quantities);

    if (clack.button_id === "") {
        clack.clickable = "no_button";
    }
    else if (clack.unknown !== "") {
        clack.clickable = "unknown";
    }
    else if (clack.bump_max) {
        clack.clickable = "bump_max";
    }
    else if (clack.high_rate) {
        clack.clickable = "high_rate";
    }
    else if (clack.high_cost) {
        clack.clickable = "high_cost";
    }
    else {
        clack.clickable = "OK";
    }

    if (clack.cost !== "Cost not found" && clack.make !== "Make not found" && clack.need !== "Need not found") {
        clack.details = "";
    }

    return;
}

function trsob_2_clacksob(trs_ob) {
    "use strict";
    var clack;
    var trs_array = Object.entries(trs_ob);
    var clacks_array = trs_array.map(function([pane_title, trs]) {
        if (DEBUG) {console.log("DEBUG GMO", pane_title);}
        var clacks = trs.map(function(tr) {
            // console.log("DEBUG idx", "tr", tr)
            clack = tr_2_clack_raw(tr, pane_title);
            return clack;
        })
        .filter((ob) => ob !== null)
        .flat()
        ;
        return [pane_title, clacks];
    });
    var clacks_ob = Object.fromEntries(clacks_array);
    return clacks_ob;
}

var GLOBAL_known_skip_page = [];
function panesob_2_trsob(panes_ob, quantities) {
    "use strict";
    var NONLOCAL_pane_heading;

    function filter_not_hidden(tr) {
        tr = $( tr );
        var is_hidden = tr.hasClass("hidden");
        if (is_hidden) {
            return false;
        }
        return true;
    }

    function map_pane_to_title_and_trs(pane, pane_heading) {
        pane = $( pane );
        var trs = pane.find("tr");
        trs = jQuery_to_array(trs);
        trs = trs.filter(filter_not_hidden);
        var tr0 = trs[0];
        tr0 = $( tr0 );
        var h2 = tr0.find("h2");
        var pane_title = cleanup_substance_name(
            h2.text(),
            pane_heading
        );

        var available_substances = Object.keys(quantities);

        var known_title = (available_substances.includes(pane_title));
        if (! known_title) {
            var page_designator = NONLOCAL_pane_heading + "/" + pane_title;
            var known_skip = (GLOBAL_known_skip_page.includes(page_designator));
            if (! known_skip) {
                console.warn("Skip", page_designator);
                GLOBAL_known_skip_page.push(page_designator);
            }
            return [];
        }

        return [pane_title, trs];
    }

    function map_panes_ob_to_all_titles_and_trs(entry) {
        const [pane_headingC, panesC] = entry;
        NONLOCAL_pane_heading = pane_headingC;
        var panes_array = jQuery_to_array(panesC);
        var pane_data = panes_array.map(function(pane) {
            return map_pane_to_title_and_trs(pane, pane_headingC);
        });

        return pane_data;
    }

    var panes_ob_array = Object.entries(panes_ob);
    var trs_array = panes_ob_array
        .map(map_panes_ob_to_all_titles_and_trs)
        .flat()
        ;
    trs_array = trs_array.filter(function(row) {
        return row.length > 0;
    });
    var trs_ob = Object.fromEntries(trs_array);
    return trs_ob;
}

function get_clacks_ob(pane_descriptors, tabs_available, quantities) {
    "use strict";
    var panes_ob = panesdesc_2_panesob(pane_descriptors, tabs_available);
    var trs_ob = panesob_2_trsob(panes_ob, quantities);
    var clacks_ob = trsob_2_clacksob(trs_ob);

    return clacks_ob;
}

function filter_clacks_by(clacks_list, filter_column) {
    "use strict";

    if (clacks_list === undefined) {
        return "";
    }

    var answer_list = clacks_list.map(function(clack) {
        var filter = clack[filter_column];
        return [filter, clack];
    });

    var answer = arraysFromEntries(answer_list);

    return answer;
}

function choose_leftmost(things) {
    "use strict";
    return things[0];
}

function choose_rightmost(things) {
    "use strict";
    return things[things.length - 1];
}

function choose_random(things) {
    "use strict";
    var i = Math.floor(Math.random() * things.length);
    return things[i];
}

function filter_field_equal(clacks_list, field_name, skip_value) {
    "use strict";
    clacks_list = clacks_list.filter(function(clack) {
        if (clack[field_name] !== skip_value) {
            // console.log("FF(==) skip", field_name, skip_value, clack);
            return false;
        }
        return true;
    });
    return clacks_list;
}

function filter_field_not_equal(clacks_list, field_name, skip_value) {
    "use strict";
    clacks_list = clacks_list.filter(function(clack) {
        if (clack[field_name] === skip_value) {
            // console.log("FF(!=) skip", field_name, skip_value, clack);
            return false;
        }
        return true;
    });
    return clacks_list;
}

function choose_best_requested(clacks_list) {
    "use strict";
    var clacks_requested_by_type = filter_clacks_by(clacks_list, "type");
    var clacks_dyson = clacks_requested_by_type.dyson;
    if (clacks_dyson) {
        var dyson_stuff_clacks = filter_field_not_equal(clacks_dyson, "clean_name", "Dyson Segment");
        if (dyson_stuff_clacks.length > 0) {
            var dyson_clacks_by_make_count = filter_clacks_by(dyson_stuff_clacks, "make_count");
            var dyson_make_counts = Object.keys(dyson_clacks_by_make_count);
            var dyson_max_make_count = Math.max(...dyson_make_counts);
            var correct_dyson_to_click_jQuery = dyson_clacks_by_make_count[dyson_max_make_count];
            var correct_dyson_to_click_DOM = correct_dyson_to_click_jQuery[0];
            return correct_dyson_to_click_DOM;
        }
        var dyson_segment_clacks = filter_field_equal(clacks_dyson, "clean_name", "Dyson Segment");
        if (dyson_segment_clacks.length > 0) {
            var dyson_segment_ob = dyson_segment_clacks[0];
            return dyson_segment_ob;
        }
    }
    var clacks_by_item = filter_clacks_by(clacks_list, "make_item");
    var all_items = Object.keys(clacks_by_item);
    var random_item = choose_random(all_items);
    var clacks_with_that_item = clacks_by_item[random_item];
    // console.log('CBR(): MBI=', clacks_by_item);
    // console.log('CBR(): items=', all_items);
    // console.log('CBR(): choosing rightmost of the', clacks_with_that_item.length, 'Clacks making', random_item);
    return choose_rightmost(clacks_with_that_item);
}

function choose_best_dyson_and_desired(clack_type_dyson) {
    "use strict";

    const NOOP = ["", 0];

    var clack_dyson_by_name = filter_clacks_by(clack_type_dyson, "clean_name");

    var dyson_segment_jquery_ob = clack_dyson_by_name['Dyson Segment'];
    if (! dyson_segment_jquery_ob) {
        return NOOP;
    }
    if (! dyson_segment_jquery_ob.length) {
        return NOOP;
    }
    var dyson_segment_dom_ob = dyson_segment_jquery_ob[0];

    var dyson_segment_desired = dyson_segment_dom_ob.desired;
    var dyson_segment_current = dyson_segment_dom_ob.current;

    if (dyson_segment_desired) {
        // Already making Dyson Segments
        return NOOP;
    }

    var dyson_ring_ob = clack_dyson_by_name['Dyson Ring'];
    var dyson_swarm_ob = clack_dyson_by_name['Dyson Swarm'];
    var dyson_sphere_ob = clack_dyson_by_name['Dyson Sphere'];

    var dyson_obs = [dyson_ring_ob, dyson_swarm_ob, dyson_sphere_ob];
    var needed_list = dyson_obs.map(function(dyson_jquery_ob) {
        var dyson_dom_ob = dyson_jquery_ob[0];
        // console.log("DEBUG: dyson_ob:", dyson_dom_ob);
        var ob_desired = dyson_dom_ob.desired;
        var cost_per_each = dyson_dom_ob.cost.dyson_segments;
        return ob_desired * cost_per_each;
    });
    var needed_total = sum(needed_list);
    var need_to_add = needed_total - dyson_segment_current;
    // console.log("DEBUG: dyson question: segment_ob=", dyson_segment_dom_ob);
    // console.log("DEBUG: dyson question: needed=", needed_list, "sum=", needed_total, "dyson_current=", dyson_segment_current, "add=", need_to_add);
    if (need_to_add > 0) {
        // console.log("DEBUG: dyson clicking (?)", dyson_segment_jquery_ob, need_to_add);
        return [dyson_segment_dom_ob, need_to_add];
    }

    return NOOP;
}

function choose_best_unrequested(clacks_list) {
    "use strict";

    // var verify_no_storage_upgrades = filter_field_equal(clacks_list, "name", "Storage Upgrade");
    // if (verify_no_storage_upgrades.length) {
    //     tick_stop();
    //     console.error('throwing an error: verify_no_storage_upgrades=', verify_no_storage_upgrades);
    //     throw new Error('we have storage upgrades here');
    // }

    // TODO: use a better method
    return choose_random(clacks_list);
}

function choose_best_gain(clack_type_gain, quantities) {
    "use strict";
    // console.warn('DEBUG: clack_type_gain:', clack_type_gain);
    var gains_with_counts = clack_type_gain.map(function(gain_ob) {
        // console.warn('  DEBUG: gain_ob:', gain_ob);
        if (gain_ob === undefined) {
            console.error("  DEBUG: no because no gain object", gain_ob);
            return [];
        }
        if (gain_ob.type === undefined) {
            var new_gain_ob = gain_ob[0];           // translate jquery->DOM object
            if (new_gain_ob === undefined) {
                console.error("  DEBUG: no because type and [0] undefined", gain_ob);
                return [];
            }

            gain_ob = new_gain_ob;
        }
        // console.log("DEBUG: gain_ob", gain_ob);
        var high_cost = gain_ob.high_cost;
        if (high_cost !== "") {
            // console.log("  DEBUG: no because high cost");
            return [];
        }
        var substance = gain_ob.pane_title;
        var substance_ob = quantities[substance];
        if (! substance_ob) {
            // console.log("  DEBUG: no because no quantity object");
            return [];
        }
        // console.log("  => DEBUG: substance_ob", substance_ob);
        var rate = substance_ob.rate;
        if (rate) {
            // console.log("  DEBUG: no because yes rate");
            return [];
        }
        var max = substance_ob.max;
        var count = substance_ob.count;
        if (count >= max) {
            // console.log("  DEBUG: no because max");
            return [];
        }
        return [gain_ob, count];
    })
    .filter(filter_not_empty)
    ;
    // console.log("DEBUG: gains_with_counts=", gains_with_counts);
    var all_counts = gains_with_counts.map(function(entry) {
        var count = entry[1];
        return count;
    });
    // console.log("  DEBUG: all_counts=", all_counts);
    if (! all_counts.length) {
        // console.log("DEBUG: no gains found");
        return "";
    }
    var min_count = Math.min(...all_counts);
    // console.log("  DEBUG: min_count=", min_count);
    var matching_gains = gains_with_counts.map(function(entry) {
        const [gainC, countC] = entry;
        var gain = gainC;
        if (countC !== min_count) {
            gain = "";
        }
        return gain;
    })
    .filter(filter_not_empty)
    ;
    // console.log("  DEBUG: matching_gains=", matching_gains);

    return choose_random(matching_gains);
}

function suppress_unused_fn_msgs() {
    "use strict";
    if (false) {
        choose_leftmost();
        choose_rightmost();
        filter_field_equal();
        filter_field_not_equal();
        suppress_unused_fn_msgs();
    }
}

function get_all_clacks(tabs_available, quantities) {
    "use strict";
    var clacks_ob = get_clacks_ob(pane_descriptors, tabs_available, quantities);
    // console.warn('clacks_ob (before):', clacks_ob);

    var clacks_entries = safeEntries(clacks_ob);
    clacks_entries.forEach(function(entry) {
        const [pane_title, clacks_list] = entry;
        clacks_list.forEach(function(clack) {
            // console.warn('DEBUG: updating clack', 'pane_title', pane_title, 'clack', clack);
            update_clack_fields(clack, pane_title, quantities);
        });
    });
    // console.warn('clacks_ob (after):', clacks_ob);

    return clacks_ob;
}

function colorize_clacks_by_clickable(clacks_by_clickable, all_click_classes) {
    "use strict";

    var filtered;

    filtered = clacks_by_clickable.no_button || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "no_button", 'to class', "no_button");
    filtered.forEach(function(clack) {
        // console.log('debug; clack (no button)', clack);
        var tr_id = clack.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "no_button", all_click_classes);
        // console.log("tr_id", tr_id, "class", "no_button", "tr", tr);
        set_display_value(clack.display_id, "");
        set_ob_title_by_string(tr, "No button");
        // set_ob_title_blank(tr);
    });

    filtered = clacks_by_clickable.unknown || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "unknown", 'to class', "unknown_substance");
    filtered.forEach(function(clack) {
        // console.log('debug; clack (unknown)', clack);
        var tr_id = clack.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "unknown_substance", all_click_classes);
        // console.log("tr_id", tr_id, "class", "unknown_substance", "tr", tr);

        var pop_up = safeEntries(clack.unknown).map(function(entry) {
            const [substance, count] = entry;
            return "Unknown: " + substance + ": " + from_number(count);
        });
        set_display_value(clack.display_id, pop_up[0]);
        set_ob_title_by_array(tr, pop_up);
    });

    filtered = clacks_by_clickable.bump_max || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "bump_max", 'to class', "bump_max");
    filtered.forEach(function(clack) {
        // console.log('debug; clack (bump max)', clack);
        var tr_id = clack.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "bump_max", all_click_classes);
        // console.log("tr_id", tr_id, "class", "bump_max", "tr", tr);

        var pop_up = safeEntries(clack.bump_max).map(function(entry) {
            const [substance, count] = entry;
            return substance + ": " + from_number(count);
        });
        set_display_value(clack.display_id, pop_up[0]);
        pop_up.unshift("Bump max:");
        set_ob_title_by_array(tr, pop_up);
    });

    filtered = clacks_by_clickable.high_cost || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "high_cost", 'to class', "high_cost");
    filtered.forEach(function(clack) {
        // console.log('debug; clack (high cost)', clack);
        var tr_id = clack.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "high_cost", all_click_classes);
        // console.log("tr_id", tr_id, "class", "high_cost", "tr", tr);

        var high_cost_time = clack.high_cost_time;
        var max_time = 0;
        var max_substance = "";
        var pop_up = safeEntries(clack.high_cost).map(function(entry) {
            const [substance, count] = entry;

            var cost_time = high_cost_time[substance];
            if (cost_time === "INF") {
                max_time = cost_time;
                max_substance = substance;
            } else if (max_time !== "INF") {
                if (cost_time > max_time) {
                    max_time = cost_time;
                    max_substance = substance;
                }
            }

            return substance + ": " + from_number(count) + " (" + toElapsedTime(cost_time) + ")";
        });
        set_display_value(clack.display_id, toHHMMSS(max_time) + " " + max_substance);
        pop_up.unshift("High cost:");
        pop_up.push("");
        pop_up.push("MAX: " + toElapsedTime(max_time));
        set_ob_title_by_array(tr, pop_up);
    });

    filtered = clacks_by_clickable.high_rate || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "high_rate", 'to class', "high_rate");
    filtered.forEach(function(clack) {
        // console.log('debug; clack (high rate/sec)', clack);
        var tr_id = clack.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "high_rate", all_click_classes);
        // console.log("tr_id", tr_id, "class", "high_rate", "tr", tr);

        var pop_up = safeEntries(clack.high_rate).map(function(entry) {
            const [substance, count] = entry;
            return substance + ": " + from_number(count);
        });
        set_display_value(clack.display_id, pop_up[0]);
        pop_up.unshift("High rate/sec:");
        set_ob_title_by_array(tr, pop_up);
    });

    return;
}

function colorize_clacks_by_requested(ok_requested, ok_UNrequested, all_click_classes) {
    "use strict";

    // console.warn('filter: setting', ok_requested.length, 'items of type', "requested: yes", 'to class', "click_me");
    ok_requested.forEach(function(clack) {
        // console.log('debug; clack (requested yes)', clack);
        var tr_id = clack.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "click_me", all_click_classes);
        // console.log("tr_id", tr_id, "class", "click_me", "tr", tr);

        set_display_value(clack.display_id, "");
        set_ob_title_by_string(tr, "Okay: requested");
        // set_ob_title_blank(tr);
    });

    // console.warn('filter: setting', ok_UNrequested.length, 'items of type', "requested: no", 'to class', "click_me_maybe");
    ok_UNrequested.forEach(function(clack) {
        // console.log('debug; clack (requested no)', clack);
        var tr_id = clack.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "click_me_maybe", all_click_classes);
        // console.log("tr_id", tr_id, "class", "click_me_maybe", "tr", tr);

        set_display_value(clack.display_id, "");
        set_ob_title_by_string(tr, "Okay: NOT requested");
        // set_ob_title_blank(tr);
    });

    return;
}

function perform_click(clack, all_click_classes) {
    "use strict";

    var tr = $( "#" + clack.tr_id );
    add_class_remove_others(tr, "clicking", all_click_classes);
    var button = $( "#" + clack.button_id );
    var input = $( "#" + clack.input_id );
    var desired = clack.desired;
    // console.log('... tr', tr, 'desired', desired, 'button', button, 'input', input);

    var click_time;
    click_time = Math.floor(new Date().getTime() / 1000);

    var elapsed_s = (click_time - prior_cick_time);
    var TIME = toElapsedTime(elapsed_s);
    TIME = "(" + TIME.trim() + ")";

    button.click();

    prior_cick_time = click_time;

    desired -= 1;
    if (! desired) {
        desired = "";
    }

    console.log("AUTO-CLICK", TIME, /* GLOBAL_pane_heading, **/ clack.pane_title, clack.name, "(" + clack.desired + "->" + desired + ")");

    input.val(desired);

    return;
}

function perform_auto_request(clack, desired, all_click_classes) {
    "use strict";

    var tr = $( "#" + clack.tr_id );
    add_class_remove_others(tr, "auto_request", all_click_classes);
    // var button = $( "#" + clack.button_id );
    var input = $( "#" + clack.input_id );
    // console.log('... tr', tr, 'desired', clack.desired, 'input', input);
    if (clack.desired) {
        console.error("Error!  'desired' is not zero/blank!", clack.desired);
        return;
    }
    if (clack.pane_title === undefined) {
        console.error("AUTO-REQUEST", "invalid clack:", clack);
        return;
    }

    console.warn("AUTO-REQUEST", /* TIME, */ clack.pane_title, clack.name, "(" + clack.desired + "->" + desired + ")");
    input.val(desired);

    return;
}

function choose_and_perform_action(
    ok_normal_requested,
    ok_normal_UNrequested,
    clack_type_dyson,
    clack_type_gain,
    clack_type_storage,
    substances_that_need_bumping,
    quantities,
    all_click_classes
) {
    "use strict";

    var clack;
    var desired;

    if (TEST) { console.log('TEST: ok_normal_requested=', ok_normal_requested); }
    if (ok_normal_requested.length) {
        clack = choose_best_requested(ok_normal_requested);

        perform_click(clack, all_click_classes);

        return;
    }

    const [clackC, desiredC] = choose_best_dyson_and_desired(clack_type_dyson);
    if (TEST) { console.log('TEST: [clackC, desiredC]=', [clackC, desiredC]); }
    if (clackC) {
        // console.log("DEBUG: performing auto_request");
        perform_auto_request(clackC, desiredC, all_click_classes);
        return;
    }

    if (TEST) { console.log('TEST: clack_type_storage=', clack_type_storage); }
    if (clack_type_storage.length) {
        var possibles = clack_type_storage.filter(function(clack) {
            if (clack.desired) {
                // desired is already set: ignore
                return false;
            }
            var substance = clack.pane_title;
            var bump_this_substance = substances_that_need_bumping.hasOwnProperty(substance);
            if (! bump_this_substance) {
                // no need to bump
                return false;
            }
            return true;
        });

        if (possibles.length) {
            clack = choose_random(possibles);
            var substance = clack.pane_title;
            desired = substances_that_need_bumping[substance];
            perform_auto_request(clack, desired, all_click_classes);
            return;
        }
    }

    if (TEST) { console.log('TEST: ok_normal_UNrequested=', ok_normal_UNrequested); }
    if (ok_normal_UNrequested.length) {
        clack = choose_best_unrequested(ok_normal_UNrequested);

        if (clack && auto_request) {
            desired = 1;
            perform_auto_request(clack, desired, all_click_classes);
            return;
        }
    }

    if (TEST) { console.log('TEST: clack_type_gain=', clack_type_gain); }
    if (clack_type_gain.length > 0) {
        // console.log("NO CLICK, try clicking a Gain button?");

        clack = choose_best_gain(clack_type_gain, quantities);
        if (clack && auto_gain) {
            desired = 1;
            perform_auto_request(clack, desired, all_click_classes);
            return;
        }
    }

    // console.log("NO CLICK, no fallback");

    return;
}

function get_bump_reasons(clacks_by_clickable) {
    "use strict";

    var bump_max = clacks_by_clickable.bump_max || [];
    // console.warn('bump_max:', bump_max);

    var bump_max_data = bump_max.map(
        function(clack) {
            var pane_title = clack.pane_title;
            var pane_name = clack.name;
            var bump_max_items = safeEntries(clack.bump_max);
            var bump_max_arr = bump_max_items.map(function(entry) {
                const [substance, count] = entry;
                // var pane_heading = "Unknown";
                // return [substance, [pane_heading + '/' + pane_title + '/' + pane_name, count]];
                return [substance, [pane_title + '/' + pane_name, count]];
            });
            // console.log('debug: bump_max_arr', bump_max_arr);
            return bump_max_arr;
        }
    )
    .flat();

    // console.log('debug: bump_max_data', bump_max_data);

    var overflow_reasons = arraysFromEntries(bump_max_data);
    // console.log('debug: overflow_reasons', overflow_reasons);

    return overflow_reasons;
}

function get_storage_numbers(clack_by_type) {
    "use strict";
    var storage_obs = clack_by_type.storage || [];
    var storage_numbers_entries = storage_obs.map(function(clack) {
        var substance = clack.pane_title;
        var desired = clack.desired;
        return [substance, desired];
    });
    var storage_numbers = Object.fromEntries(storage_numbers_entries);
    return storage_numbers;
}

function doublings_between(from_val, to_val) {
    "use strict";
    var answer = 0;
    while (from_val < to_val) {
        from_val *= 2;
        answer += 1;
    }
    return answer;
}

function colorize_left_bar(quantities, overflow_reasons, storage_numbers) {
    "use strict";

    var all_overflow_classes = ["bump_my_max", "already_bumped"];

    var substances_that_need_bumping = {};

    safeEntries(quantities).forEach(function(quant) {
        const [substance, leftbar_tab] = quant;

        if (leftbar_tab.pane !== "Resources") {
            // console.warn('debug: overflow SKIP substance', substance);
            return;
        }
        // console.warn('debug: overflow substance', substance);
        // console.log('debug: overflow leftbar_tab', leftbar_tab);

        var overflow_reasons_arr = overflow_reasons[substance] || [];
        // var overflow_reasons_arr = overflow_reasons ? (overflow_reasons[substance] || []) : [];
        // console.log('debug: overflow overflow_reasons_arr', overflow_reasons_arr);

        var max_multiplier = 0;

        var reason_arr = overflow_reasons_arr.map(function(item) {
            const [reason, count] = item;
            var max = leftbar_tab.max;
            if (! max) { return "[no max]"; }
            max = to_number(max);
            var multiplier = doublings_between(max, count);
            max_multiplier = Math.max(multiplier, max_multiplier);
            return reason + ": " + from_number(count) + " (" + multiplier + " x)";
        });
        // console.log('debug: overflow reason_arr', reason_arr);

        var tr = $( '#' + leftbar_tab.tr_id );
        var overflow_class = "";
        if (reason_arr.length) {
            if (storage_numbers[substance]) {
                overflow_class = "already_bumped";
            } else {
                overflow_class = "bump_my_max";
                substances_that_need_bumping[substance] = max_multiplier;
            }
        }
        // console.log('debug: overflow overflow_class', overflow_class);
        add_class_remove_others(tr, overflow_class, all_overflow_classes);

        set_ob_title_by_array(tr, reason_arr);
    });

    return substances_that_need_bumping;
}

// global variable
var tick_id;

function tick() {
    "use strict";
    // console.log("tick", tick_id);

    var tabs_available = get_tabs_available();
    // console.log("tabs_available:", tabs_available);

    var quantities = get_quantities(tabs_available);
    if (TEST) { console.log("quantities:", quantities); }

    check_energy_levels(quantities);

    var clacks_ob = get_all_clacks(tabs_available, quantities);
    var all_clacks_list = Object.values(clacks_ob).flat();
    var clacks_by_clickable = filter_clacks_by(all_clacks_list, "clickable");

    if (TEST) { console.log('clacks_by_clickable:', clacks_by_clickable); }

    var all_click_classes = [
        "bump_max",
        "high_cost",
        "high_rate",
        "click_me",
        "click_me_maybe",
        "clicking",
        "auto_request",
        "unknown_substance",
        "no_button"
    ];

    colorize_clacks_by_clickable(clacks_by_clickable, all_click_classes);

    var clack_by_requested = filter_clacks_by(clacks_by_clickable.OK, "click_requested");
    if (TEST) { console.log('clack_by_requested:', clack_by_requested); }

    var clack_by_type = filter_clacks_by(all_clacks_list, "type");

    var ok_requested   = clack_by_requested[1] || [];
    var ok_UNrequested = clack_by_requested[0] || [];

    var clack_type_gain    = clack_by_type.gain    || [];
    var clack_type_storage = clack_by_type.storage || [];
    var clack_type_dyson   = clack_by_type.dyson   || [];

    colorize_clacks_by_requested(ok_requested, ok_UNrequested, all_click_classes);

    // var ok_normal_requested = filter_field_equal(ok_requested, "type", "normal");
    var ok_normal_UNrequested = filter_field_equal(ok_UNrequested, "type", "normal");

    var overflow_reasons = get_bump_reasons(clacks_by_clickable);
    var storage_numbers = get_storage_numbers(clack_by_type);

    var substances_that_need_bumping = colorize_left_bar(quantities, overflow_reasons, storage_numbers);

    choose_and_perform_action(
        ok_requested,
        ok_normal_UNrequested,
        clack_type_dyson,
        clack_type_gain,
        clack_type_storage,
        substances_that_need_bumping,
        quantities,
        all_click_classes
    );

    if (TEST) {
        safeEntries(clacks_by_clickable).forEach(function([clacks_label, clacks_list]) {
            // also should check by cost:

            var check_by_make = filter_clacks_by(clacks_list, "make");
            var check_by_need = filter_clacks_by(clacks_list, "need");
            var fail_make = check_by_make["Make not found"];
            var fail_need = check_by_need["Need not found"];
            if (fail_make !== undefined) { console.error(clacks_label, 'fail_make:', fail_make); }
            if (fail_need !== undefined) { console.error(clacks_label, 'fail_need:', fail_need); }

            var clack_by_make = filter_clacks_by(clacks_list, "make_item");
            // console.log(clacks_label, 'by_make_item:', clack_by_make);
            var fail_make_item = clack_by_make["ERROR: make.length > 1"];
            if (fail_make_item !== undefined) { console.error(clacks_label, 'fail make_item:', fail_make_item); }

        });

        var clack_by_cost = filter_clacks_by(all_clacks_list, "cost");
        var clack_by_make = filter_clacks_by(all_clacks_list, "make");
        var clack_by_need = filter_clacks_by(all_clacks_list, "need");
        var fail_cost = clack_by_cost["Cost not found"] || [];
        var fail_make = clack_by_make["Make not found"] || [];
        var fail_need = clack_by_need["Need not found"] || [];
        // if (fail_cost !== undefined) { console.error('ALL', 'fail_cost:', fail_cost); }
        // if (fail_make !== undefined) { console.error('ALL', 'fail_make:', fail_make); }
        // if (fail_need !== undefined) { console.error('ALL', 'fail_need:', fail_need); }
        console.log('clack_by_type:', clack_by_type);

        var clack_by_make_item = filter_clacks_by(all_clacks_list, "make_item");
        // console.log(clacks_label, 'clack_by_make_item:', clack_by_make_item);
        var fail_make_item = clack_by_make_item["ERROR: make.length > 1"] || [];
        // if (fail_make_item !== undefined) { console.error('ALL', 'fail make_item:', fail_make_item); }

        var all_problems = [].concat(
            fail_cost,
            fail_make,
            fail_need,
            fail_make_item,
            []  // last: no comma
        );
        if (all_problems.length > 0) { console.error('ALL', 'all_problems:', all_problems); }
        var all_details_entries = all_problems.map(function(ob) {
            var name = ob.name;
            var details = ob.details;
            return [name, details];
        });
        var all_details = Object.fromEntries(all_details_entries);
        if (all_problems.length > 0) { console.warn('ALL', 'all_details:', all_details); }
    }

    return;
}

function tick_stop() {
    "use strict";
    if (tick_id) {
        clearInterval(tick_id);
        console.warn("tick stop", tick_id);
        tick_id = 0;
    }
}

function tick_start() {
    "use strict";
    var tick_milliseconds = tick_seconds * 1000;
    if (tick_id) {
        tick_stop();
    }
    tick_id = setInterval(tick, tick_milliseconds);
    console.warn("tick start", tick_id);
}

if (DEBUG_tick) {
    tick_stop();
    tick();
} else {
    tick_start();
}

function test() {
    "use strict";

    TEST = true;
    // console.warn('test(): setting TEST to', TEST);

    tick();

    TEST = false;
    // console.warn('test(): setting TEST to', TEST);

    return;
}


function x_CONSUME() {
    "use strict";
    x_CONSUME();
    test();
}
