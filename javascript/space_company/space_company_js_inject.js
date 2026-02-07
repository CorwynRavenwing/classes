// JavaScript to auto-run the game "Space Company":
// https://sparticle999.github.io/SpaceCompany/

/*jslint devel*/        // allow console.log()
/*jslint white */       // allow odd whitespace
/*global $ */           // jQuery defines "$"

var tick_seconds = 1;

var DEBUG = false;
var DEBUG_tick = false;
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
    Wonders:        "#wonder",
    ZZZ:            "LAST: NO COMMA"
};

var GLOBAL_known_unknowns = [];
var GLOBAL_tabs_available = [];
var GLOBAL_known_missing_tabs = [];
var GLOBAL_available_substances = [];
var GLOBAL_available_substances_by_page = {};
var GLOBAL_known_skip_page = [];

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
    switch(multiplier_str) {
        case "":    multiplier = 1;             break;  // 1 thousand
        case "K":   multiplier = 1000;          break;  // 1 thousand
        case "M":   multiplier = 1000000;       break;  // 1 million
        case "B":   multiplier = 1000000000;    break;  // 1 billion
        case "T":   multiplier = 1000000000000; break;  // 1 trillion
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
            // console.warn("Skip used ID '" + id + "'");
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

    $.each(classList, function(remove_idx, remove_me) {
        remove_idx = remove_idx;
        if (remove_me !== className) {
            ob.removeClass(remove_me);
        }
    });
}

function panesdesc_2_allowed(pane_descriptors) {
    "use strict";
    var pane_entries = Object.entries(pane_descriptors);

    var panes_allowed = pane_entries.filter(function(entry) {
        const [pane_heading, pane_desc] = entry;
        if (DEBUG) { console.log("debug: entry", entry, "values", pane_heading, pane_desc); }

        var available = GLOBAL_tabs_available.includes(pane_heading);
        if (! available) {
            if (DEBUG) {console.warn("Skip unavailable tab", pane_heading);}
            return false;
        }
        return true;
    });

    return panes_allowed;
}

function panesdesc_2_left_trs() {
    "use strict";

    var panes_allowed = panesdesc_2_allowed(pane_descriptors);

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

function cleanup_substance_name(name) {
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
    substance.tr_id = tr_id;
    return substance;
}

function get_quantities() {
    "use strict";
    var leftbar = panesdesc_2_left_trs();

    var leftbar_entries = Object.entries(leftbar);

    var substance_list_all = leftbar_entries.map(function(entry) {
        const [pane_heading, trs] = entry;
        // console.log('GQ(): pane_heading, trs', pane_heading, trs);
        var tds_list = trs.map(function(tr) {
            var tds = tr_to_tds(tr);
            return tds;
        });
        // console.log('GQ() tds_list', tds_list);

        var texts_list = tds_list.map(function(entry) {
            const [tr_id, td] = entry;
            // console.warn('    gq(): tr_id', tr_id, 'td', td);
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
    // console.warn('GQ(): substance_list_all', substance_list_all);

    // // should pull these counts from the Interstellar:Rockets page
    var plating_count = 0;
    var engine_count = 0;
    var section_count = 0;
    substance_list_all.push( textlist_2_substance("Rocket Parts (fake)", "NONE", ["Shield Plating", plating_count, 50]) );
    substance_list_all.push( textlist_2_substance("Rocket Parts (fake)", "NONE", ["Engine Unit", engine_count, 25]) );
    substance_list_all.push( textlist_2_substance("Rocket Parts (fake)", "NONE", ["Aerodynamic Sections", section_count, 15]) );

    var quantities_list = substance_list_all.map(function(substance) {
        var name_clean = cleanup_substance_name(substance.name);
        return [name_clean, substance];
    });
    // console.warn('GQ(): quantities_list', quantities_list);

    var quantities = Object.fromEntries(quantities_list);
    console.warn('GQ(): quantities', quantities);
    return quantities;
}

function x() {
    "use strict";
    return get_quantities();
}

function for_each_nav(fn, argument) {
    "use strict";
    var answer = [];

    var sidetabs = $("#resourceNavParent > tbody > tr");
    $.each(sidetabs, function(index, value) {
        var ob = $( value );
        index = index;   // ignore
        // is_sidetab = ob.hasClass("sideTab");
        // if (! is_sidetab) {
        //     return;
        // }
        answer.push( fn(ob, argument) );
    });

    return answer;
}

function get_one_max(tr) {
    "use strict";
    tr = $( tr );
    var is_hidden = tr.hasClass("hidden");
    if (is_hidden) {
        // console.warn("max: hidden", tr);
        return [];
    }
    // console.log(tr);
    var tds = tr.children();
    var label = $( tds[1] ).text().trim().toLowerCase();
    if (! label) {
        // console.warn("max: no label", label);
        return [];
    }
    var values = $( tds[3] ).children();
    var quant = $( values[1] ).text().trim();
    quant = to_number(quant);

    // console.log(label, "<=", quant);
    return [label, quant];
}




/// ############################################################################




function check_energy_levels_old() {
    "use strict";
    var energy_change_ob = $("#energyps");
    var energy_falling_case = energy_change_ob.hasClass("red");

    var energy_deficit_ob = $("#energyLow");
    var energy_okay_case = energy_deficit_ob.hasClass("hidden");
    var energy_deficit_case = (! energy_okay_case);

    var game_ob = $("#game");
    if (energy_deficit_case) {
        game_ob.addClass("energy-deficit");
        game_ob.removeClass("energy-falling");
        game_ob.removeClass("energy-okay");
    } else if (energy_falling_case) {
        game_ob.addClass("energy-falling");
        game_ob.removeClass("energy-deficit");
        game_ob.removeClass("energy-okay");
    } else {
        game_ob.addClass("energy-okay");
        game_ob.removeClass("energy-deficit");
        game_ob.removeClass("energy-falling");
    }
}

function check_energy_levels_new() {
    "use strict";
}

function check_energy_levels() {
    "use strict";   
    var use_new = false;

    if (use_new) {
        check_energy_levels_new();
    } else {
        check_energy_levels_old();
    }
}

function get_available_substances(maxes) {
    "use strict";
    var answer = [];
    var NONLOCAL_tab_desc;

    $.each(maxes, function(max_item) {
        answer.push(max_item);
    });

    function get_one_available(index, tr) {
        index = index;  // ignore
        tr = $( tr );
        var is_hidden = tr.hasClass("hidden");
        if (is_hidden) {
            return;
        }
        var tds = tr.children("td");
        var first = $( tds[0] );
        if( first.children("img").length ) {
            if (tds.length === 1) {
                console.error("available_substances: image in only TD", tds);
                return;
            }
            first = $( tds[1] );
        }

        var text = cleanup_substance_name(
            first.text()
        );
        if (! text) {
            return;
        }
        answer.push( text );
        if (DEBUG) { console.log("TD:", text); }
        GLOBAL_available_substances_by_page[NONLOCAL_tab_desc].push("'" + text + "'");
    }

    function scan_one_tab(tab_idx, tab) {
        tab_idx = tab_idx;
        tab = $( tab );
        // console.log("DEBUG: tab", tab_idx, tab);

        var trs = tab.children("table").children("tbody").children("tr");
        $.each(trs, get_one_available);
    }

    $.each(pane_descriptors, function(pane_heading, tab_desc) {
        var available = GLOBAL_tabs_available.includes(pane_heading);
        if (! available) {
            if (DEBUG) { console.warn("Skip unavailable tab", pane_heading); }
            return;
        }
        if (DEBUG) { console.log("Check tab", pane_heading); }

        var tabs = $( tab_desc + " > .container");
        if (DEBUG) { console.warn("tabs:", tab_desc, tabs); }
        NONLOCAL_tab_desc = pane_heading;
        GLOBAL_available_substances_by_page[NONLOCAL_tab_desc] = [];
        $.each(tabs, scan_one_tab);
    });

    return answer;
}

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

function get_maxes() {
    "use strict";
    var max_pairs = for_each_nav(get_one_max, null);
    // console.log(max_pairs);
    var science_ob = $("#science");
    var science_value = science_ob.text();
    science_value = to_number(science_value);
    var science_max = (10 * science_value);      // actually unlimited

    var fuel_ob = $("#rocketFuel");
    var fuel_value = fuel_ob.text();
    fuel_value = to_number(fuel_value);
    var fuel_max = (10 * fuel_value);      // actually unlimited

    var rockets_max = 1000;     // NOTE: not sure how to compute this

    var dark_ob = $("#stargazeNavdarkMatter_count");
    var dark_value = dark_ob.text();
    dark_value = to_number(dark_value);
    var dark_max = (10 * dark_value);      // actually unlimited

    var maxes = {
        science: science_max,
        // should pull these maxes from the Interstellar:Rockets page
        shield_plating: 50,
        engine_unit: 25,
        aerodynamic_sections: 15,
        // should pull these maxes from the Solar System tab
        rocket: rockets_max,
        rocket_fuel: fuel_max,
        dark_matter: dark_max,      // NOTE: unclear why this is necessary
        ZZZ: "LAST: NO COMMA"
    };

    $.each(max_pairs, function(pair_idx, max_pair) {
        pair_idx = pair_idx;
        if (max_pair.length === 0) {
            // console.log("get_maxes: SKIP", pair_idx, max_pair)
            return;
        }
        const [label, quant] = max_pair;
        // console.log("get_maxes: ok", label, quant);
        maxes[label] = quant;
    });
    return maxes;
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

    string = string.trim();

    return string;
}

function extract_costs_from_details(orig_string, pane_heading, pane_title, purchase) {
    "use strict";
    var string = orig_string;
    // const cost_flag = "Costs";

    if (pane_title === "energy_mass_conversion") {
        // does not have Costs section
        return [];
    }
    if (pane_title === "dyson swarms and sphere") {
        // has non-standard Costs section
        return [];
    }
    if (purchase === "Rocket Ship: Built") {
        // does not have Costs section anymore
        return [];
    }
    if (pane_title === "travel") {
        // Interstellar.
        // does not have Costs section
        return [];
    }
    if (string === "") {
        // string is now blank: no costs
        return [];
    }

    var position = string.search(cost_flag);
    if (DEBUG) {console.log("Costs Position:", position);}
    if (position === -1) {
        var label = pane_heading + "/" + pane_title + "/" + purchase;
        throw new Error("Costs not found:\n" + label + "\n'" + orig_string + "'\n---\n'" + string + "'");
    }
    position += cost_flag.length;
    string = string
        .slice(position)            // delete up to after "Costs"
        .replace(/^:/, "")          // remove leading colon
        .trim()                     // remove lead/trail spaces
        .replace(/[.]+$/, "")       // remove trailing period
        .replaceAll(/\ \ +/g, " ")  // no doubled spaces
        ;

    // if (GLOBAL_pane_title === "inside the wonder station") {
    //     console.log(orig_string)
    //     console.log(string)
    // }

    var costs = string.split(", ");     // split on "comma space"
    return costs;
}

function panesdesc_2_panesob(pane_descriptors) {
    "use strict";
    var panes_allowed = panesdesc_2_allowed(pane_descriptors);
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

function check_tabs(maxes, available_substances) {
    "use strict";
    // var cost_flag = "Costs";
    var GLOBAL_overflow_reasons = {};
    var GLOBAL_pane_heading;
    var GLOBAL_pane_title;
    var GLOBAL_purchase;
    var GLOBAL_unknown_substances;
    var GLOBAL_bump_specifics;
    var GLOBAL_clicked_something = false;

    // console.log(panes)

    function scan_one_cost(cost_idx, cost_str) {
        if (cost_str === "") {
            // no costs (energy-mass conversion page): NOOP
            return;
        }
        if (cost_idx === "format") {
            // why are functions being passed in here ?!?
            return;
        }
        // console.log("cost_str:", cost_idx, cost_str)
        var cost_split = cost_str
            .replaceAll(" ", "_")       // any number of spaces -> underscore
            .replace("_", " ")          // first underscore -> space again
            .split(" ", 2)              // split on that first space
            ;
        // console.log("cost split:", cost_split);
        const [neededC, substanceC] = cost_split;
        var needed = to_number(neededC);
        var substance = substanceC.toLowerCase();
        if (substance === "gem") { substance = "gems"; }
        var known_substance = Object.keys(maxes).includes(substance);
        if (! known_substance) {
            GLOBAL_unknown_substances.push("'" + substance + "'");
            var seen = (GLOBAL_known_unknowns.includes(substance));
            if (! seen) {
                GLOBAL_known_unknowns.push(substance);
                /* if (DEBUG) */ console.warn("cost of UNKNOWN SUBSTANCE:", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, cost_idx, "'" + cost_str + "'", substance, needed);
            }
            return;
        }
        var max_value = maxes[substance];
        if (needed <= max_value) {
            // console.log("cost ok:", cost_idx, substance, needed, max_value);
            return;
        }

        if (GLOBAL_purchase.includes("Swarm:")) {
            console.warn("Swarm (scan_one_cost)", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase);
            return;
        }

        var known_overflow_reasons = Object.keys(GLOBAL_overflow_reasons).includes(substance);
        if (! known_overflow_reasons) {
            GLOBAL_overflow_reasons[substance] = [];
        }
        GLOBAL_overflow_reasons[substance].push(
            GLOBAL_pane_heading + "/" + GLOBAL_pane_title + "/" + GLOBAL_purchase + ": " + from_number(needed)
        );
        GLOBAL_bump_specifics.push(substance);
    }

    function scan_one_tr(tr_idx, tr) {
        tr_idx = tr_idx;
        tr = $( tr );
        var h3 = tr.find("h3");
        GLOBAL_purchase = h3
            .text()
            .trim()
            .replace(new RegExp("/[0-9]*$"), "")  // remove "/NN" from end
            .replace(new RegExp(": [0-9]*$"), "")   // remove ": NN" from end
            ;
        if (! GLOBAL_purchase) {
            return;
        }
        // NOTE: delete next section:
        var is_hidden = tr.hasClass("hidden");
        if (is_hidden) {
            if (DEBUG) { console.warn(GLOBAL_pane_title, GLOBAL_purchase, "HIDDEN"); }
            return;
        }
        // NOTE: end deleted section
        if (GLOBAL_purchase.includes("Swarm:")) {
            console.warn("Swarm (scan_one_tr)", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase);
            console.warn("tr", tr);
        }
        if (GLOBAL_pane_title === "energy_mass_conversion") {
            return;
        }
        if (GLOBAL_pane_title === "dyson_swarms_and_sphere") {
            return;
        }
        var cant_click = false;
        // console.log("tr:", tr_idx, tr);
        var details = tr
            .find("td > span")
            .text()
            .trim();
        var current_ob = h3
            .find("span");
        var current = current_ob
            .text()
            .trim();
        var td = tr.find("td");
        var button = td
            .find("button")
            [0];
        if (! button) {
            button = td
                .find("div.btn")
                [0];
        }
        if (button) {
            button = $( button );
        }
        if (button) {
            if (button.hasClass("destroy")) {
                console.error("destroy button!", button);
                button = null;
            }
        }
        // yes, repeat the prior question
        if (button) {
            if (button.hasClass("btn-warning")) {
                button = null;
            }
        }
        // yes, repeat the prior question
        if (button) {
            var button_is_hidden = button
                .hasClass("hidden");
            if (button_is_hidden) {
                // console.warn("button is hidden", button);
                button = null;
            } else {
                button_is_hidden = button
                    .parent()
                    .hasClass("hidden");
                if (button_is_hidden) {
                    // console.warn("button is hidden", button.parent());
                    button = null;
                }
            }
        }
        var input = td
            .find("input.desired");
        if (button && (input.length === 0)) {
            // console.warn(GLOBAL_pane_title, GLOBAL_purchase, "Creating input object:");
            input = $("<input type='textbox' class='desired'/>");
            td.append(input);
        }
        var desired = "";
        if (input) {
            var val = input.val();
            if (val) {
                desired = val.trim();
            }
        }
        desired = to_number(desired);
        // if (current && desired) {
        //     console.log(pane_title, purchase, "current", current, "desired", desired);
        // }
        var red_ingredients = tr
            .find("td > span span.red");
        if (red_ingredients.length) {
            // console.log("red_ingredients", red_ingredients);
            cant_click = true;
        }
        if (DEBUG) { console.log("purchase:", GLOBAL_purchase); }
        details = cleanup_details(details);
        // if (DEBUG)  console.log("details:", details);
        var costs = extract_costs_from_details(details, GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase);
        if (DEBUG) { console.log("costs:", costs); }
        GLOBAL_unknown_substances = [];
        GLOBAL_bump_specifics = [];
        $.each(costs, scan_one_cost);
        var pop_up = [];
        var set_class = "";

        var all_click_classes = [
            "bump_max",
            "cant_click",
            "click_me",
            "clicking",
            "unknown_substance",
            "no_button",
            "ZZZ_LAST_NO_COMMA"
        ];

        if (! button) {
            set_class = "no_button";
        } else {
            if (desired) {
                if (! button) {
                    console.warn("Trying to click missing button", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase);
                    cant_click = true;
                }
                if (cant_click) {
                    set_class = "cant_click";
                    pop_up.push("Missing Ingredients: " + red_ingredients.length);
                } else {
                    if (GLOBAL_clicked_something) {
                        set_class = "click_me";
                    } else {
                        set_class = "clicking";
                    }
                }
            }

            if (GLOBAL_bump_specifics.length) {
                set_class = "bump_max";
                pop_up.push("Bump:");
                pop_up.push(...GLOBAL_bump_specifics);
            }
            if (GLOBAL_unknown_substances.length) {
                pop_up.push("Unknown:");
                pop_up.push(...GLOBAL_unknown_substances);
                set_class = "unknown_substance";
            }
            if (set_class === "clicking") {
                // if (red_ingredients.length) {
                //     console.warn("red_ingredients", red_ingredients)
                //     console.warn("cant_click:", cant_click)
                // }
                var click_time;
                click_time = Math.floor(new Date().getTime() / 1000);

                var elapsed_s = (click_time - prior_cick_time);
                var TIME = toHHMMSS(elapsed_s);
                TIME = "(" + TIME.trim() + ")";

                button.click();
                var new_current = current_ob.text().trim();
                var VERIFY = false;
                if (VERIFY && (current !== "") && (new_current === current)) {
                    console.warn("ERROR: tried clicking", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, "no change", new_current, current);
                    set_class = "click_me";
                    // need to remove click-me from removal list
                } else {
                    GLOBAL_clicked_something = true;

                    console.log("AUTO-CLICK", TIME, GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, "(" + desired + ")");

                    prior_cick_time = click_time;

                    desired -= 1;
                    if (! desired) {
                        desired = "";
                    }
                    input.val(desired);
                }
            }
        }

        add_class_remove_others(tr, set_class, all_click_classes);

        if (pop_up.length) {
            var reasons = pop_up
                .join("\n");
            tr.prop("title", reasons);
        } else {
            tr.prop("title", "");
        }
    }

    function scan_one_pane(pane_idx, pane) {
        pane_idx = pane_idx;
        pane = $(pane);
        var trs = pane.find("tr");
        var tr0 = $( trs[0] );
        var h2 = tr0.find("h2");
        GLOBAL_pane_title = cleanup_substance_name(
            h2.text()
        );
        
        var known_title = (available_substances.includes(GLOBAL_pane_title));
        if (! known_title) {
            var page_designator = GLOBAL_pane_heading + "/" + GLOBAL_pane_title;
            var known_skip = (GLOBAL_known_skip_page.includes(page_designator));
            if (! known_skip) {
                console.warn("Skip", page_designator);
                GLOBAL_known_skip_page.push(page_designator);
            }
            return;
        }
        if (GLOBAL_pane_title === "dyson_swarms_and_sphere") {
            // console.warn("Ignore Dyson Swarm / Sphere pane");
            return;
        }
        if (DEBUG) {
            console.log("pane:", pane);
            console.log(trs);
            console.log("tr0:", tr0);
            console.log("h2:", h2);
            console.log("pane_title:", GLOBAL_pane_title);
        }
        $.each(trs, scan_one_tr);
    }

    var panes_ob = panesdesc_2_panesob(pane_descriptors);
    $.each(panes_ob, function(pane_heading, panes) {
        GLOBAL_pane_heading = pane_heading;
        if (DEBUG) {console.log("pane_heading:", GLOBAL_pane_heading);}
        if (DEBUG) {console.warn("panes:", panes);}
        $.each(panes, scan_one_pane);
    });

    // console.log("overflow_reasons", GLOBAL_overflow_reasons);
    return GLOBAL_overflow_reasons;
}

function prices_2_pair(cost_str) {
    "use strict";
    if (cost_str === "") {
        return [];
    }
    // console.log("cost_str:", cost_str)
    var cost_split = cost_str
        .replaceAll(" ", "_")       // any number of spaces -> underscore
        .replace("_", " ")          // first underscore -> space again
        .split(" ", 2);             // split on that first space
    // console.log("cost split:", cost_split)
    const [neededC, substanceC] = cost_split;
    var needed = to_number(neededC);
    var substance = substanceC.toLowerCase();
    if (substance === "gem") { substance = "gems"; }
    var cost = [substance, needed];
    // console.log("cost:", cost);
    return cost;
}

function priceslist_2_pricesob(prices_list) {
    "use strict";
    var prices_arr = prices_list.map(prices_2_pair);
    var prices_ob = Object.fromEntries(prices_arr);
    return prices_ob;
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
        // console.warn("button is hidden", button);
        return "";
    }

    button_is_hidden = button
        .parent()
        .hasClass("hidden");

    if (button_is_hidden) {
        // console.warn("button parent is hidden", button.parent())
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
        // console.warn(debug_label, "Creating input object:")
        input = $("<input type='textbox' class='desired'/>");
        td.append(input);
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
    return uniqueId(input, 'input');
}

function complain_about_unknown_substances_once(unknown_substances_list) {
    "use strict";
    var answers = unknown_substances_list.map(function(substance) {
        var seen = (GLOBAL_known_unknowns.includes(substance));
        if (! seen) {
            GLOBAL_known_unknowns.push(substance);
            return true;
        }
        return false;
    });
    if (DEBUG) { console.warn('DEBUG: complain answers', answers); }
    return;
}

function get_unknown_substances(costs_ob, maxes) {
    "use strict";
    var costs_list = Object.entries(costs_ob);

    var unknown_substances_list = costs_list.map(function([substance, quant]) {
        quant = quant;
        return substance;
    }).filter(function(substance) {
        var known_substance = Object.keys(maxes).includes(substance);
        return (! known_substance);
    });

    return unknown_substances_list;
}

function get_bump_max_ob(costs_ob, maxes) {
    "use strict";
    var costs_list = Object.entries(costs_ob);

    var bump_max_list = costs_list.filter(function([substance, needed]) {
        var max_value = maxes[substance];
        return (needed > max_value);
    });
    if (bump_max_list.length > 0) {
        var bump_max_ob = Object.fromEntries(bump_max_list);
        return bump_max_ob;
    } else {
        return "";   // or maybe {} or []
    }
}

// XYZZY:
function tr_2_magic(tr, maxes, pane_title) {
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
        .replace(new RegExp("/[0-9]*$"), "")  // remove "/NN" from end
        .replace(new RegExp(": [0-9]*$"), "")   // remove ": NN" from end
        ;

    if (! purchase) {
        return null;
    }
    magic.name = purchase;

    var is_hidden = tr.hasClass("hidden");
    if (is_hidden) {
        /* if (DEBUG) */ console.warn(pane_title, purchase, "HIDDEN");
        return;
    }

    if (pane_title === "energy_mass_conversion") {
        return null;
    }
    if (pane_title === "dyson_swarms_and_sphere") {
        return null;
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

    var desired = inputid_2_desired(input_id);
    magic.desired = desired;

    details = cleanup_details(details);
    var costs = extract_costs_from_details(details, "missing_pane_heading", pane_title, purchase);

    if (DEBUG) {console.log("purchase:", purchase);}
    if (DEBUG) {console.log("costs:", costs);}
    costs = priceslist_2_pricesob(costs);
    if (DEBUG) {console.log("costs:", costs);}
    magic.costs = costs;

    var unknown_substances = get_unknown_substances(costs, maxes);
    magic.unknown = unknown_substances;
    complain_about_unknown_substances_once(unknown_substances);
    if (unknown_substances.length) {
        /* if (DEBUG) */ console.warn("cost of UNKNOWN SUBSTANCES:", pane_title, purchase, unknown_substances);
    }

    var bump_maxes = get_bump_max_ob(costs, maxes);
    magic.bump_max = bump_maxes;

    if (magic.unknown_substances) {
        magic.class = "unknown_substance";
    }
    else if (magic.bump_max) {
        magic.class = "bump_max";
    }
    // ... more ...
    else {
        magic.class = "OK";
    }
    // ### MOVE TO HERE ... vvv


    return magic;
}

function trsob_2_magicsob(trs_ob, maxes) {
    "use strict";
    var magic;
    var trs_array = Object.entries(trs_ob);
    var magics_array = trs_array.map(function([pane_title, trs]) {
        if (DEBUG) {console.log("DEBUG GMO", pane_title);}
        var magics = trs.map(function(tr) {
            // console.log("DEBUG idx", "tr", tr)
            magic = tr_2_magic(tr, maxes, pane_title);
            return magic;
        }).filter((ob) => ob !== null);
        return [pane_title, magics];
    });
    var magics_ob = Object.fromEntries(magics_array);
    return magics_ob;
}

// function check_known_substance(substance, maxes) {
//     "use strict";
//     // NOTE: BROKEN, BUT NOT CALLED FROM ANYWHERE
//     // if (! known_substance) {
//     // }
//     return known_substance;
// }

function panesob_2_trsob(panes_ob, available_substances) {
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

    function map_pane_to_title_and_trs(pane) {
        pane = $( pane );
        var trs = pane.find("tr");
        trs = jQuery_to_array(trs);
        trs = trs.filter(filter_not_hidden);
        var tr0 = trs[0];
        tr0 = $( tr0 );
        var h2 = tr0.find("h2");
        var pane_title = cleanup_substance_name(
            h2.text()
        );

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
        // NOTE: delete this section, move logic to next function
        // if (pane_title === "dyson_swarms_and_sphere") {
        //     // console.warn("Ignore Dyson Swarm / Sphere pane");
        //     return [];
        // }
        // NOTE: end deleted section

        return [pane_title, trs];
    }

    function map_panes_ob_to_all_titles_and_trs(entry) {
        const [pane_headingC, panesC] = entry;
        NONLOCAL_pane_heading = pane_headingC;
        var panes_array = jQuery_to_array(panesC);
        var pane_data = panes_array.map(map_pane_to_title_and_trs);
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

function test() {
    "use strict";

    // the following variables and functions have been copied in from check_tabs:
    var GLOBAL_overflow_reasons = {};
    var GLOBAL_pane_heading;
    var GLOBAL_pane_title;
    var GLOBAL_purchase = "h3.something.text.etc";
    var GLOBAL_unknown_substances;
    var GLOBAL_bump_specifics;
    var GLOBAL_clicked_something = false;

    function xCONSUME_scan_one_cost(cost_idx, cost_str, maxes) {
        cost_idx = cost_idx;
        if (cost_str === "") {
            // no costs: NOOP
            return;
        }
        // console.log("cost_str:", cost_idx, cost_str);
        const [substance, needed] = prices_2_pair(cost_str);

        var max_value = maxes[substance];
        if (needed <= max_value) {
            // console.log("cost ok:", cost_idx, substance, needed, max_value)
            return;
        }

        if (GLOBAL_purchase.includes("Swarm:")) {
            console.warn("Swarm (scan_one_cost)", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase);
            return;
        }

        var known_overflow_reasons = Object.keys(GLOBAL_overflow_reasons).includes(substance);
        if (! known_overflow_reasons) {
            GLOBAL_overflow_reasons[substance] = [];
        }
        GLOBAL_overflow_reasons[substance].push(
            GLOBAL_pane_heading + "/" + GLOBAL_pane_title + "/" + GLOBAL_purchase + ": " + from_number(needed)
        );
        GLOBAL_bump_specifics.push(substance);
    }

    function xCONSUME_scan_one_tr(tr_idx, tr) {
        tr_idx = tr_idx;
        var costs = "defined in deleted section";

        // ### MOVE FROM HERE ... ^^^


        var cant_click = false;
        // if (current && desired) {
        //     console.log(pane_title, purchase, "current", current, "desired", desired)
        // }
        var red_ingredients = tr
            .find("td > span span.red");
        if (red_ingredients.length) {
            // console.log("red_ingredients", red_ingredients)
            cant_click = true;
        }
        GLOBAL_unknown_substances = [];
        GLOBAL_bump_specifics = [];
        $.each(costs, xCONSUME_scan_one_cost);
        var pop_up = [];
        var set_class = "";

        var all_click_classes = [
            "bump_max",
            "cant_click",
            "click_me",
            "clicking",
            "unknown_substance",
            "no_button",
            "ZZZ_LAST_NO_COMMA"
        ];

        var button = "defined in deleted section";
        var desired = "defined in deleted section";
        var current = "defined in deleted section";
        var current_ob = "defined in deleted section";
        var input = "defined in deleted section";

        if (! button) {
            set_class = "no_button";
        } else {
            if (desired) {
                if (! button) {
                    console.warn("Trying to click missing button", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase);
                    cant_click = true;
                }
                if (cant_click) {
                    set_class = "cant_click";
                    pop_up.push("Missing Ingredients: " + red_ingredients.length);
                } else {
                    if (GLOBAL_clicked_something) {
                        set_class = "click_me";
                    } else {
                        set_class = "clicking";
                    }
                }
            }

            if (GLOBAL_bump_specifics.length) {
                set_class = "bump_max";
                pop_up.push("Bump:");
                pop_up.push(...GLOBAL_bump_specifics);
            }
            if (GLOBAL_unknown_substances.length) {
                pop_up.push("Unknown:");
                pop_up.push(...GLOBAL_unknown_substances);
                set_class = "unknown_substance";
            }
            if (set_class === "clicking") {
                // if (red_ingredients.length) {
                //     console.warn("red_ingredients", red_ingredients)
                //     console.warn("cant_click:", cant_click)
                // }
                var click_time;
                click_time = Math.floor(new Date().getTime() / 1000);

                var elapsed_s = (click_time - prior_cick_time);
                var TIME = toHHMMSS(elapsed_s);
                TIME = "(" + TIME.trim() + ")";

                button.click();
                var new_current = current_ob.text().trim();
                var VERIFY = false;
                if (VERIFY && (current !== "") && (new_current === current)) {
                    console.warn("ERROR: tried clicking", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, "no change", new_current, current);
                    set_class = "click_me";
                    // need to remove click-me from removal list
                } else {
                    GLOBAL_clicked_something = true;

                    console.log("AUTO-CLICK", TIME, GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, "(" + desired + ")");

                    prior_cick_time = click_time;

                    desired -= 1;
                    if (! desired) {
                        desired = "";
                    }
                    input.val(desired);
                }
            }
        }

        if (set_class) {
            tr.addClass(set_class);
        }
        $.each(all_click_classes, function(remove_idx, remove_me) {
            remove_idx = remove_idx;
            if (remove_me !== set_class) {
                tr.removeClass(remove_me);
            }
        });
        if (pop_up.length) {
            var reasons = pop_up
                .join("\n");
            tr.prop("title", reasons);
        } else {
            tr.prop("title", "");
        }
    }

    function xCONSUME() {
        xCONSUME();
        xCONSUME_scan_one_cost();
        xCONSUME_scan_one_tr();
    }
    // end copied section

    var quantities = get_quantities();
    quantities = quantities;            // WRITE ME

    var maxes = get_maxes();
    var available_substances = get_available_substances(maxes);
    var panes_ob = panesdesc_2_panesob(pane_descriptors);
    var trs_ob = panesob_2_trsob(panes_ob, available_substances);
    var magics_ob = trsob_2_magicsob(trs_ob, maxes);

    if (true) { return magics_ob; }

    $.each(trs_ob, function(pane_title, trs) {
        GLOBAL_pane_heading = "UNKNOWN";
        GLOBAL_pane_title = pane_title;
        console.warn("DEBUG: each trs_ob", GLOBAL_pane_title, "trs:", trs);
        $.each(trs, xCONSUME_scan_one_tr);
    });
}

// xyzzy

function colorize_one_max(tr, tab_data) {
    "use strict";
    tr = $( tr );
    var is_hidden = tr.hasClass("hidden");
    if (is_hidden) {
        return false;
    }
    // console.log(tr);
    var tds = tr.children();
    var label = $( tds[1] )
        .text()
        .trim()
        .toLowerCase()
        ;
    var is_overflow = Object.keys(tab_data).includes(label);
    if (is_overflow) {
        tr.addClass("bump_max");
        var reasons = tab_data[label]
            .join("\n");
        tr.prop("title", reasons);
        return [label, "yes"];
    } else {
        tr.removeClass("bump_max");
        tr.prop("title", "");
        return [label, "no"];
    }
}

// global variable
var tick_id;

function tick() {
    "use strict";
    // console.log("tick", tick_id);
    check_energy_levels();

    GLOBAL_tabs_available = get_tabs_available();
    // console.log("GLOBAL_tabs_available:", GLOBAL_tabs_available);
    var maxes = get_maxes();
    // console.log("maxes:", maxes);
    var available_substances = get_available_substances(maxes);
    // console.log("available_substances:", available_substances);
    GLOBAL_available_substances = available_substances;
    var tab_data = check_tabs(maxes, available_substances);
    // console.log("tab_data", tab_data);
    var results = for_each_nav(colorize_one_max, tab_data);
    if (DEBUG) {console.log("results", results);}
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
    x();
    test();
    GLOBAL_available_substances = GLOBAL_available_substances;
}
