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
// var TEST = false;

var prior_cick_time;

var cost_flag = "Costs";    // actually a const, injector cant re-declare them

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
    var hours   = Math.floor(total_sec / 3600);
    var minutes = Math.floor(total_sec / 60) % 60;
    var seconds = total_sec % 60;

    if (hours) { hours += " hour"; } else { hours = ""; }
    if (minutes) { minutes += " min"; } else { minutes = ""; }
    if (seconds) { seconds += " sec"; } else { seconds = ""; }

    var answer = [hours,minutes,seconds];

    return answer.join(" ");
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
    const ID = "id";
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
        .replace("dyson segments", "dyson swarms and sphere")
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
        if (DEBUG) {
            console.error('Plasma', pane_heading, name);
        }
    }

    return cleanup_substance_name_simple(name);
}

function textlist_2_substance(pane_heading, tr_id, texts) {
    "use strict";
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
            console.error("GQ():", pane_heading, "3-element texts for invalid tab name '" + substance.name + "'", "texts", texts, "substance", substance);
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

    return substance;
}

function get_quantities(tabs_available) {
    "use strict";
    var leftbar = panesdesc_2_left_trs(tabs_available);

    var leftbar_entries = Object.entries(leftbar);

    var substance_list_all = leftbar_entries.map(function(entry) {
        const [pane_heading, trs] = entry;
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
            return substance;
        });

        return substance_list;
    }).flat();
    if (DEBUG) {console.log('GQ(): substance_list_all', substance_list_all);}

    // // should pull these counts from the Interstellar:Rockets page
    var plating_count = 0;
    var engine_count = 0;
    var section_count = 0;
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
    // IF (DEBUG) {console.log('GQ(): quantities', quantities);}
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

function cleanup_details(string) {
    "use strict";
    // var cost_flag = "Costs";

    // Wonder phrases before costs:
    string = string.replace("He requires that you donate", cost_flag);
    string = string.replace("He requests a pyramid containing", cost_flag);
    string = string.replace("He requests a tower consisting of", cost_flag);
    string = string.replace("The Overlord wishes for a cube made up of", cost_flag);

    // alternate cost flag
    string = string.replace("This requires", cost_flag);
    string = string.replace("Cost:", cost_flag);

    // Wonder phrases within costs:
    string = string.replaceAll(" and ", ", ");

    // Wonder phrases after costs:
    string = string.replace(" for this knowledge", "");
    string = string.replace(" to acquire his methods", "");
    string = string.replace(" to unlock this technology", "");
    string = string.replace(" to be given this technology", "");

    // Wonder phrases to clean up:
    string = string.replace("Donate Resources", "");
    string = string.replace(/Activate\ .*/, "");
    string = string.replace(/Rebuild\ .*/, "");
    string = string.replace("Unlock Plasma Research", "");
    string = string.replace("Unlock EMC Machine Research", "");
    string = string.replace("Unlock Dyson Sphere Research", "");
    string = string.replace(/[0-9.]+%$/, "");

    // Dark Matter phrases to clean up:
    string = string.replaceAll(/Improves\ relationship\ by\ [0-9.]+/g, "");
    string = string.replaceAll(/Improves\ relationship\ by/g, "");

    // Uses/Produces phrase to clean up:
    string = string.replace("They produce", "produces");
    string = string.replace("produces a lot of power", "");
    string = string.replace("produces Gems at intense speeds", "");
    string = string.replace("uses nano-fibres", "");
    string = string.replace("Uses fission to create large amounts of power", "");

    string = string.trim();

    return string;
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
    var prices_list = prices_str.split(", ");       // split on "comma space"
    var prices_arr = prices_list.map(price_2_pair);
    var prices_ob = Object.fromEntries(prices_arr);
    return prices_ob;
}

function extract_text_between(haystack, start_needle, end_needle_list) {
    "use strict";
    var answer = haystack.toLowerCase();
    var position = answer.search(start_needle.toLowerCase());
    if (position === -1) {
        return null;
    }
    position += start_needle.length;
    answer = answer.slice(position);    // delete up to after "needle"

    end_needle_list.forEach(function(end_needle) {
        var end_pos = answer.search(end_needle.toLowerCase());
        if (end_pos === -1) {
            return;
        }
        answer = answer.slice(0, end_pos);
    });

    answer = answer
        .replace(/^:/, "")          // remove leading colon
        .trim()                     // remove trailing spaces
        .replace(/[.]+$/, "")       // remove trailing period
        .trim()                     // remove trailing spaces *again*
        .replaceAll(/\ \ +/g, " ")  // no doubled spaces
        ;
    return answer;
}

function extract_costs_from_details(orig_string, pane_title, purchase, label) {
    "use strict";
    const start_needle = cost_flag;
    const end_needle_list = [];

    if (pane_title === "energy_mass_conversion") {
        if (purchase !== "Research") {
            // does not have Costs section
            return "";
        }
    }
    if (pane_title === "dyson swarms and sphere") {
        if (purchase !== "Research") {
            // has non-standard Costs section
            return "";
        }
    }
    if (purchase === "Rocket Ship: Built") {
        // does not have Costs section anymore
        return "";
    }
    if (pane_title === "travel") {
        // Interstellar.
        // does not have Costs section
        return "";
    }
    if (orig_string === "") {
        // string is now blank: no costs
        return "";
    }

    var string = extract_text_between(orig_string, start_needle, end_needle_list);
    if (string === null) {
        throw new Error("Costs not found:\n" + label + "\n'" + orig_string + "'\n---\n'" + string + "'");
    }

    // console.log('prices:', string, label);
    var prices = prices_2_priceob(string);
    return prices;
}

function extract_requires_from_details(orig_string, pane_title, purchase, label) {
    "use strict";

    const start_needle = "Uses";
    const end_needle_list = ["per second", "every second", "each second", " for ", ", produces "];       // ", provides"];

    const purchase_ignore = [
        "Batteries",
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
        "Plasma Storage Units",
        "Rocket Droid",
        "Scout Ship",
        "Small Pump",
        "Solar Panels",
        "Storage Upgrade",
        "Vacuum Cleaner",
        "Woodcutter",
        // -----
        "Energy Efficiency",
        "Resource Efficiency",
        "Science Efficiency",
        // -----
        "Activate Wonder",
        "Energetic Wonder",
        "Meteorite Wonder",
        "Precious Metals Wonder",
        "Technological Wonder",
        "ZZZ LAST NO COMMA"
    ];
    const pane_ignore = [
        "science",
        "ZZZ LAST NO COMMA"
    ];

    if (pane_ignore.includes(pane_title)) {
        return "";
    }

    if (purchase_ignore.includes(purchase)) {
        return "";
    }

    var string = extract_text_between(orig_string, start_needle, end_needle_list);
    if (string === null) {
        string = extract_text_between(orig_string, "They use", end_needle_list);
    }
    if (string === null) {
        var try_string = extract_text_between(orig_string, "produces", []);         // grab the whole "produces x for y" part
        if (try_string !== null) {
            string = extract_text_between(try_string, " for ", end_needle_list);    // then jump to the "for", take the rest
        }
    }
    // yes, ask again:
    if (string === null) {
        // throw new Error("Requires not found:\n" + label + "\n'" + orig_string + "'\n---\n'" + string + "'");
        label = label;  // ignore
        return "Requires not found";
    }

    // console.log('prices:', "'"+orig_string+"'", "'"+string+"'", label);
    var prices = prices_2_priceob(string);
    return prices;
}

function extract_provides_from_details(orig_string, pane_title, purchase, label) {
    "use strict";
    const start_needle = "produces";
    const end_needle_list = ["per second", "every second", "each second", " for ", ", uses "];   // , ", requires"];

    const purchase_ignore = [
        "Grinder",
        "Batteries",
        "Plasma Storage Units",
        "Storage Upgrade",
        // -----
        "Energy Efficiency",
        "Resource Efficiency",
        "Science Efficiency",
        // -----
        "Activate Wonder",
        "Energetic Wonder",
        "Meteorite Wonder",
        "Precious Metals Wonder",
        "Technological Wonder",
        "ZZZ LAST NO COMMA"
    ];

    if (purchase_ignore.includes(purchase)) {
        return "";
    }
    pane_title = pane_title;    // ignore

    var string = extract_text_between(orig_string, start_needle, end_needle_list);
    if (string === null) {
        // throw new Error("Provides not found:\n" + label + "\n'" + orig_string + "'\n---\n'" + string + "'");
        label = label;  // ignore
        return "Provides not found";
    }

    // console.log('prices:', "'"+orig_string+"'", "'"+string+"'", label);
    var prices = prices_2_priceob(string);
    return prices;
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

function get_button_id(td) {
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

    if (button.hasClass("destroy")) {
        console.error("destroy button!", button);
        return "";
    }

    if (button.hasClass("btn-warning")) {
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

    return uniqueId(button, 'btn');
}

function inputid_2_desired(input_id) {
    "use strict";
    var desired = "";
    if (input_id) {
        var val = $("#" + input_id).val();
        if (val) {
            desired = val.trim();
        }
    }
    return to_number(desired);
}

function create_input_and_get_id(td, button_id, debug_label) {
    "use strict";
    var input = td
        .find("input.desired");

    if (input.length === 0) {
        // "input" not found
        if (! button_id) {
            // no button or input --> okay
            return;
        }
        // button but no input: create input
        // console.log(debug_label, "Creating input object:")
        input = $("<input type='textbox' class='desired'/>");
        td.append(input);
    } else {
        // "input" is found
        if (! button_id) {
            // input but no button: input is obsolete
            console.log(debug_label, "Destroying input object:");
            input.remove();
        // } else {
        //     // both button and input: okay
        }
    }
    return uniqueId(input, 'input');
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

function get_unknown_substances(costs_ob, quantities) {
    "use strict";

    var costs_list = Object.keys(costs_ob);

    var unknown_substances_list = costs_list.filter(function(substance) {
        var known_substance = Object.keys(quantities).includes(substance);
        return (! known_substance);
    });
    if (unknown_substances_list.length > 0) {
        return unknown_substances_list;
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

function get_high_cost_ob(costs_ob, quantities) {
    "use strict";
    var costs_list = Object.entries(costs_ob);

    var high_cost_list = costs_list.filter(function([substance, needed]) {
        var item_ob = quantities[substance];
        if (item_ob === undefined) {
            // no such substance: problem
            return true;
        }
        var count_value = item_ob.count;
        if (count_value === "") {
            console.log('DEBUG: checking high cost for non-counted substance', substance, 'needed', needed, 'count', count_value);
            // no count -> no problem
            return false;
        }
        return (needed > count_value);
    });
    if (high_cost_list.length > 0) {
        var high_cost_ob = Object.fromEntries(high_cost_list);
        return high_cost_ob;
    } else {
        return "";
    }
}

function get_high_rate_ob(rates_ob, quantities) {
    "use strict";
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

function tr_2_magic(tr, pane_title, quantities) {
    "use strict";
    var magic = {};
    // console.log("tr2magic", tr);
    tr = $( tr );
    magic.tr_id = uniqueId(tr, 'tr-right');

    // console.log("->", tr);
    var h3 = tr.find("h3");
    var purchase = h3
        .text()
        .trim()
        .replace(new RegExp("/[0-9]*$"), "")    // remove "/NN" from end
        .replace(new RegExp(": [0-9]*$"), "")   // remove ": NN" from end
        ;

    if (! purchase) {
        return null;
    }
    magic.name = purchase;

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
    if (pane_title === "dyson_swarms_and_sphere") {
        if (purchase !== "Research") {
            // this is where we wire in the special Dyson Sphere code
            return null;
        }
    }

    var details = tr
        .find("td > span")
        .text()
        .trim()
        ;

    var current_ob = h3
        .find("span");
    var current = current_ob
        .text()
        .trim();
    magic.current = to_number(current);

    var td = tr.find("td");

    var button_id = get_button_id(td);
    magic.button_id = button_id;

    var input_id = create_input_and_get_id(td, button_id, pane_title + "/" + purchase);
    magic.input_id = input_id;

    magic.desired = inputid_2_desired(input_id);
    magic.click_requested = ((magic.desired > 0) ? 1 : 0);

    details = cleanup_details(details);

    var label = pane_title + "/" + purchase;
    var costs = extract_costs_from_details(details, pane_title, purchase, label);
    magic.costs = costs;

    var clean_purchase = purchase
        .replace(' / ', '')
        .replace(/[0-9]+$/, '')
        .replace(/^Tier\ [0-9]+\ /, '')
        .replace(/^T[0-9]+\ /, '')
        .replace(/#$/, '')
        .trim();

    magic.requires = extract_requires_from_details(details, pane_title, clean_purchase, label);
    magic.provides = extract_provides_from_details(details, pane_title, clean_purchase, label);

    var unknown_substances = [].concat(
        get_unknown_substances(magic.requires, quantities),
        get_unknown_substances(magic.provides, quantities),
        get_unknown_substances(costs, quantities),
        []  // last, no comma
    ).filter(function(item) {
        return item !== "";
    });
    complain_about_unknown_substances_once(unknown_substances);
    if (unknown_substances.length) {
        if (DEBUG) { console.warn("cost of UNKNOWN SUBSTANCES:", pane_title, purchase, unknown_substances); }
    } else {
        unknown_substances = "";
    }
    magic.unknown = unknown_substances;
    
    magic.bump_max = get_bump_max_ob(costs, quantities);

    magic.high_cost = get_high_cost_ob(costs, quantities);

    magic.high_rate = get_high_rate_ob(magic.requires, quantities);

    magic.provides = (magic.provides === "") ? {} : magic.provides;
    magic.provides.DEBUG = 'DEBUG';
    // console.warn('DEBUG: magic.provides', magic.provides);
    var provides_entries = Object.entries(magic.provides);
    var provides_entry;
    // console.warn('DEBUG: provides_entries', provides_entries);
    // console.warn('DEBUG: provides_entries.length', provides_entries.length);
    switch(provides_entries.length) {
      case 0:
        magic.provides_item = "";
        magic.provides_count = 0;
        break;
      case 1:
        provides_entry = provides_entries[0];

        magic.provides_item = provides_entry[0];
        magic.provides_count = provides_entry[1];
        break;
      default:
        magic.provides_item = "ERROR: provides.length > 1";
        magic.provides_count = provides_entries.length;
    } 

    if (magic.button_id === "") {
        magic.clickable = "no_button";
    }
    else if (magic.unknown !== "") {
        magic.clickable = "unknown";
    }
    else if (magic.bump_max) {
        magic.clickable = "bump_max";
    }
    else if (magic.high_cost) {
        magic.clickable = "high_cost";
    }
    else if (magic.high_rate) {
        magic.clickable = "high_rate";
    }
    else {
        magic.clickable = "OK";
    }

    magic.pane_title = pane_title;

    // magic.details = details;

    /*
        magic = {
          "name": "Storage Upgrade",
          "pane_title": "Metal"

          "current": 0,
          "desired": 25,        // == actually "how many MORE should we get"
          "click_requested": 1, // == 1 if desired > 0

          "costs": {
            "helium": 50,
            "lunarite": 20
          },

          "unknown": [],
          "bump_max": "",
          "high_cost": "",
          "high_rate": "",
          "clickable": "OK"

          "button_id": "uniq-btn-28",
          "input_id": "uniq-input-29",
          "tr_id": "heliumStorageUpgrade",
        };
    */
    return magic;
}

function trsob_2_magicsob(trs_ob, quantities) {
    "use strict";
    var magic;
    var trs_array = Object.entries(trs_ob);
    var magics_array = trs_array.map(function([pane_title, trs]) {
        if (DEBUG) {console.log("DEBUG GMO", pane_title);}
        var magics = trs.map(function(tr) {
            // console.log("DEBUG idx", "tr", tr)
            magic = tr_2_magic(tr, pane_title, quantities);
            return magic;
        }).filter((ob) => ob !== null);
        return [pane_title, magics];
    });
    var magics_ob = Object.fromEntries(magics_array);
    return magics_ob;
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

function get_magics_ob(pane_descriptors, tabs_available, quantities) {
    "use strict";
    var panes_ob = panesdesc_2_panesob(pane_descriptors, tabs_available);
    var trs_ob = panesob_2_trsob(panes_ob, quantities);
    var magics_ob = trsob_2_magicsob(trs_ob, quantities);

    return magics_ob;
}

function filter_magics_by(magics_list, filter_column) {
    "use strict";

    var answer_list = magics_list.map(function(magic) {
        var filter = magic[filter_column];
        return [filter, magic];
    });

    var answer = arraysFromEntries(answer_list);

    return answer;
}

function choose_best_requested(magics_list) {
    "use strict";
    // TODO: blindly picking the leftmost for now
    return magics_list[0];
}

function choose_best_unrequested(magics_list) {
    "use strict";

    magics_list = magics_list.filter(function(magic) {
        if (magic.name === "Storage Upgrade") {
            // console.log('   ... skip Storage upgrade', magic);
            return false;
        }
        return true;
    });
    // TODO: blindly picking a random one for now
    var i = Math.floor(Math.random() * magics_list.length);
    return magics_list[i];
}

function get_magic_by_clickable(tabs_available, quantities) {
    "use strict";
    var magics_ob = get_magics_ob(pane_descriptors, tabs_available, quantities);
    // console.warn('magics_ob:', magics_ob);

    var magics_list = Object.values(magics_ob).flat();
    // console.warn('magics_list:', magics_list);

    var magic_by_clickable = filter_magics_by(magics_list, "clickable");
    // console.warn('magic_by_clickable:', magic_by_clickable);

    // magic_by_clickable =
    //     {
    //       "no_button": [ ... ],
    //       "unknown": [ ... ],
    //       "bump_max": [ ... ],
    //       "high_cost": [ ... ],
    //       "OK": [ ... ]
    //     };

    return magic_by_clickable;
}

function colorize_clacks_by_clickable(magic_by_clickable, all_click_classes) {
    "use strict";

    var filtered;

    filtered = magic_by_clickable.no_button || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "no_button", 'to class', "no_button");
    filtered.forEach(function(magic) {
        // console.log('debug; magic (no button)', magic);
        var tr_id = magic.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "no_button", all_click_classes);
        // console.log("tr_id", tr_id, "class", "no_button", "tr", tr);
        set_ob_title_by_string(tr, "No button");
        // set_ob_title_blank(tr);
    });

    filtered = magic_by_clickable.unknown || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "unknown", 'to class', "unknown_substance");
    filtered.forEach(function(magic) {
        // console.log('debug; magic (unknown)', magic);
        var tr_id = magic.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "unknown_substance", all_click_classes);
        // console.log("tr_id", tr_id, "class", "unknown_substance", "tr", tr);

        var pop_up = safeEntries(magic.unknown).map(function(entry) {
            const [substance, count] = entry;
            return "Unknown: " + substance + ": " + from_number(count);
        });
        set_ob_title_by_array(tr, pop_up);
    });

    filtered = magic_by_clickable.bump_max || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "bump_max", 'to class', "bump_max");
    filtered.forEach(function(magic) {
        // console.log('debug; magic (bump max)', magic);
        var tr_id = magic.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "bump_max", all_click_classes);
        // console.log("tr_id", tr_id, "class", "bump_max", "tr", tr);

        var pop_up = safeEntries(magic.bump_max).map(function(entry) {
            const [substance, count] = entry;
            return "Bump max: " + substance + ": " + from_number(count);
        });
        set_ob_title_by_array(tr, pop_up);
    });

    filtered = magic_by_clickable.high_cost || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "high_cost", 'to class', "high_cost");
    filtered.forEach(function(magic) {
        // console.log('debug; magic (high cost)', magic);
        var tr_id = magic.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "high_cost", all_click_classes);
        // console.log("tr_id", tr_id, "class", "high_cost", "tr", tr);

        var pop_up = safeEntries(magic.high_cost).map(function(entry) {
            const [substance, count] = entry;
            return "High cost: " + substance + ": " + from_number(count);
        });
        set_ob_title_by_array(tr, pop_up);
    });

    filtered = magic_by_clickable.high_rate || [];
    // console.warn('filter: setting', filtered.length, 'items of type', "high_rate", 'to class', "high_rate");
    filtered.forEach(function(magic) {
        // console.log('debug; magic (high rate/sec)', magic);
        var tr_id = magic.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "high_rate", all_click_classes);
        // console.log("tr_id", tr_id, "class", "high_rate", "tr", tr);

        var pop_up = safeEntries(magic.high_rate).map(function(entry) {
            const [substance, count] = entry;
            return "High rate/sec: " + substance + ": " + from_number(count);
        });
        set_ob_title_by_array(tr, pop_up);
    });

    return;
}

function colorize_clacks_by_requested(okay_and_requested, okay_but_not_requested, all_click_classes) {
    "use strict";

    // console.warn('filter: setting', okay_and_requested.length, 'items of type', "requested: yes", 'to class', "click_me");
    okay_and_requested.forEach(function(magic) {
        // console.log('debug; magic (requested yes)', magic);
        var tr_id = magic.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "click_me", all_click_classes);
        // console.log("tr_id", tr_id, "class", "click_me", "tr", tr);

        set_ob_title_by_string(tr, "Okay: requested");
        // set_ob_title_blank(tr);
    });

    // console.warn('filter: setting', okay_but_not_requested.length, 'items of type', "requested: no", 'to class', "click_me_maybe");
    okay_but_not_requested.forEach(function(magic) {
        // console.log('debug; magic (requested no)', magic);
        var tr_id = magic.tr_id;
        var tr = $( "#" + tr_id );
        add_class_remove_others(tr, "click_me_maybe", all_click_classes);
        // console.log("tr_id", tr_id, "class", "click_me_maybe", "tr", tr);

        set_ob_title_by_string(tr, "Okay: NOT requested");
        // set_ob_title_blank(tr);
    });

    return;
}

function click_something(okay_and_requested, okay_but_not_requested, all_click_classes) {
    "use strict";

    var magic;
    var tr;
    var button;
    var input;
    var desired;

    if (okay_and_requested.length) {
        magic = choose_best_requested(okay_and_requested);
        // console.log('CLICK ON:', magic);

        tr = $( "#" + magic.tr_id );
        add_class_remove_others(tr, "clicking", all_click_classes);
        button = $( "#" + magic.button_id );
        input = $( "#" + magic.input_id );
        desired = magic.desired;
        // console.log('... tr', tr, 'desired', desired, 'button', button, 'input', input);

        var click_time;
        click_time = Math.floor(new Date().getTime() / 1000);

        var elapsed_s = (click_time - prior_cick_time);
        var TIME = toHHMMSS(elapsed_s);
        TIME = "(" + TIME.trim() + ")";

        button.click();

        prior_cick_time = click_time;

        desired -= 1;
        if (! desired) {
            desired = "";
        }

        console.log("AUTO-CLICK", TIME, /* GLOBAL_pane_heading, **/ magic.pane_title, magic.name, "(" + magic.desired + "->" + desired + ")");

        input.val(desired);

    } else if (okay_but_not_requested.length) {
        magic = choose_best_unrequested(okay_but_not_requested);
        // console.log("NO CLICK! fall back to:", magic.name, "(skip)");

        // tr = $( "#" + magic.tr_id );
        // add_class_remove_others(tr, "auto_request", all_click_classes);
        // // button = $( "#" + magic.button_id );
        // input = $( "#" + magic.input_id );
        // console.log('... tr', tr, 'desired', magic.desired, 'input', input);
        // if (magic.desired) {
        //     console.error("Error!  'desired' is not zero/blank!", magic.desired);
        //     // return, maybe?
        // } else {
        //     desired = 1;
        //     console.log("AUTO-REQUEST", /* TIME, */ magic.pane_title, magic.name, "(" + magic.desired + "->" + desired + ")");
        //     input.val(desired);
        // }

    } else {
        console.log("NO CLICK, no fallback");
    }

    return;
}

function get_bump_reasons(magic_by_clickable) {
    "use strict";

    var bump_max = magic_by_clickable.bump_max || [];
    // console.warn('bump_max:', bump_max);

    var bump_max_data = bump_max.map(
        function(magic) {
            var pane_title = magic.pane_title;
            var pane_name = magic.name;
            var bump_max_items = safeEntries(magic.bump_max);
            var bump_max_arr = bump_max_items.map(function(entry) {
                const [substance, count] = entry;
                var pane_heading = "Unknown";
                return [substance, [pane_heading + '/' + pane_title + '/' + pane_name, count]];
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

function doublings_between(from_val, to_val) {
    "use strict";
    var answer = 0;
    while (from_val < to_val) {
        from_val *= 2;
        answer += 1;
    }
    return answer;
}

function colorize_left_bar(quantities, overflow_reasons) {
    "use strict";

    var all_overflow_classes = ["bump_max"];

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

        var reason_arr = overflow_reasons_arr.map(function(item) {
            const [reason, count] = item;
            var max = leftbar_tab.max;
            if (! max) { return "[no max]"; }
            max = to_number(max);
            var multiplier = doublings_between(max, count);
            return reason + ": " + from_number(count) + " (" + multiplier + " x)";
        });
        // console.log('debug: overflow reason_arr', reason_arr);

        var tr = $( '#' + leftbar_tab.tr_id );
        var overflow_class = (reason_arr.length ? "bump_max" : "");
        // console.log('debug: overflow overflow_class', overflow_class);
        add_class_remove_others(tr, overflow_class, all_overflow_classes);

        set_ob_title_by_array(tr, reason_arr);
    });

    return;
}



    var tabs_available = get_tabs_available();

    var quantities = get_quantities(tabs_available);
    check_energy_levels(quantities);

    var magic_by_clickable = get_magic_by_clickable(tabs_available, quantities);

    var all_click_classes = [
        "bump_max",
        "cant_click",   // deprecated
        "high_cost",
        "high_rate",
        "click_me",
        "click_me_maybe",
        "clicking",
        "auto_request",
        "unknown_substance",
        "no_button"
    ];

    colorize_clacks_by_clickable(magic_by_clickable, all_click_classes);

    var magic_by_requested = filter_magics_by(magic_by_clickable.OK, "click_requested");
    // console.warn('magic_by_requested:', magic_by_requested);

    var okay_and_requested     = magic_by_requested[1] || [];
    var okay_but_not_requested = magic_by_requested[0] || [];

    colorize_clacks_by_requested(okay_and_requested, okay_but_not_requested, all_click_classes);

    click_something(okay_and_requested, okay_but_not_requested, all_click_classes);

    var overflow_reasons = get_bump_reasons(magic_by_clickable);

    colorize_left_bar(quantities, overflow_reasons);

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

function x_CONSUME() {
    "use strict";
    x_CONSUME();
    test();
}
