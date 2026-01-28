// JavaScript to auto-run the game "Space Company":
// https://sparticle999.github.io/SpaceCompany/

var tick_seconds = 1

var DEBUG = false
var DEBUG_tick = false
var prior_cick_time

var cost_flag = "Costs"     // actually a const, but the system freaks out about re-declaring them

var pane_descriptors = {
    Resources:       '#resourceTabParent',
    Research:        '#research',
    'Solar System':  '#solarSystem',
    Wonders:         '#wonder',
    'Sol Center':    '#solCenterPage',
    'Nonexistent':   '#TestingOnly',
    // Machine:         '#machineTab',
    Interstellar:    '#interstellarTab_pane',
    Stargaze:        '#stargazeTab_pane',
}

var GLOBAL_known_unknowns = []
var GLOBAL_tabs_available = []
var GLOBAL_known_missing_tabs = []
var GLOBAL_available_substances = []
var GLOBAL_available_substances_by_page = {}
var GLOBAL_known_skip_page = []

function check_energy_levels() {
    var energy_change_ob = $('#energyps')
    var energy_falling_case = energy_change_ob.hasClass('red')

    var energy_deficit_ob = $('#energyLow')
    var energy_okay_case = energy_deficit_ob.hasClass('hidden')
    var energy_deficit_case = (! energy_okay_case)

    var game_ob = $('#game')
    if (energy_deficit_case) {
        game_ob.addClass('energy-deficit')
        game_ob.removeClass('energy-falling')
        game_ob.removeClass('energy-okay')
    } else if (energy_falling_case) {
        game_ob.addClass('energy-falling')
        game_ob.removeClass('energy-deficit')
        game_ob.removeClass('energy-okay')
    } else {
        game_ob.addClass('energy-okay')
        game_ob.removeClass('energy-deficit')
        game_ob.removeClass('energy-falling')
    }
}

function get_available_substances(maxes) {
    var answer = []
    var NONLOCAL_tab_desc

    $.each(maxes, function(max_item, max_value) {
        answer.push(max_item)
    });

    function get_one_available(index, tr) {
        tr = $( tr )
        var is_hidden = tr.hasClass('hidden')
        if (is_hidden) {
            return
        }
        var tds = tr.children('td')
        var first = $( tds[0] )
        if( first.children('img').length ) {
            if (tds.length == 1) {
                console.error('available_substances: image in only TD', tds)
                return
            }
            first = $( tds[1] )
        }

        var text = first
            .text()
            .trim()
            .toLowerCase()
            .replace('the ','')
            .replace('comms', 'communication')
            .replace('stargate', 'stargate room')
            .replace('dyson segments', 'dyson swarms and sphere')
            .replace(': dormant', '')
            .replace(': activated', '')
            .replaceAll(' ', '_');
        if (! text) {
            return
        }
        answer.push( text )
        if (DEBUG) console.log('TD:', text)
        GLOBAL_available_substances_by_page[NONLOCAL_tab_desc].push("'" + text + "'")
    }

    function scan_one_tab(tab_idx, tab) {
        tab = $( tab )
        // console.log('DEBUG: tab', tab_idx, tab)

        var trs = tab.children('table').children('tbody').children('tr')
        $.each(trs, get_one_available)
    }

    $.each(pane_descriptors, function(pane_heading, tab_desc) {
        var available = GLOBAL_tabs_available.includes(pane_heading)
        if (! available) {
            if (DEBUG) console.warn('Skip unavailable tab', pane_heading)
            return
        }
        if (DEBUG) console.log('Check tab', pane_heading)

        var tabs = $( tab_desc + ' > .container')
        if (DEBUG) console.warn('tabs:', tab_desc, tabs)
        NONLOCAL_tab_desc = pane_heading
        GLOBAL_available_substances_by_page[NONLOCAL_tab_desc] = []
        $.each(tabs, scan_one_tab)
    });

    return answer
}

function get_tabs_available() {
    var answer = []

    var tabList = $("#tabList li")
    $.each(tabList, function(index, value) {
        ob = $( value )
        var hidden = ob.is(':hidden');
        if (hidden) {
            return
        }
        var pull_right = ob.hasClass('pull-right');
        if (pull_right) {
            return
        }
        var label = ob.text().trim()
        answer.push(label);
        var known_label = (label in pane_descriptors)
        if (! known_label) {
            if (! GLOBAL_known_missing_tabs.includes(label)) {
                console.log('VISIBLE TAB, UNKNOWN LABEL:', label)
                GLOBAL_known_missing_tabs.push(label)
            }
        }
    });

    return answer
}

function from_number(value) {
    mult_idx = 0
    while (value > 1000) {
        mult_idx += 1
        value /= 1000
    }
    value = Math.round(value * 1000) / 1000;    // round to 3 places
    value_int = Math.round(value)
    if (value == value_int) {
        value = value_int       // convert to type int if exact value
    }
    multipliers = ['', 'K', 'M', 'B', 'T', '???']
    multiplier_str = multipliers[mult_idx]
    answer = value.toString() + multiplier_str
    return answer
}

function to_number(orig_value, comment= '') {
    value = orig_value
    value = value.replaceAll(',', '')
    value = value.replaceAll('N/A', '')
    value = value.replaceAll('/', '')  // Energy comes preceeded by '/' for some reason
    value = value.trim()            // and a million spaces
    var answer = parseFloat(value)
    multiplier_str = value.replace(/^[0-9.]*/, '')
    multiplier = 1
    switch(multiplier_str) {
        case '':    multiplier = 1;                 break;
        case 'K':   multiplier = 1_000;             break;
        case 'M':   multiplier = 1_000_000;         break;
        case 'B':   multiplier = 1_000_000_000;     break;
        case 'T':   multiplier = 1_000_000_000_000; break;
        default:
            throw new Error('to_number(): Invalid multiplier "' + multiplier_str + '" (' + orig_value + '->' + value + ') ' + comment)
    } 
    // if (DEBUG) console.log('to_number:', value, multiplier_str, multiplier, answer)
    answer *= multiplier
    answer = Math.round(answer)
    return answer
}

function toHHMMSS(total_sec) {
    var hours   = Math.floor(total_sec / 3600)
    var minutes = Math.floor(total_sec / 60) % 60
    var seconds = total_sec % 60

    if (hours) { hours += ' hour' } else { hours = '' }
    if (minutes) { minutes += ' min' } else { minutes = '' }
    if (seconds) { seconds += ' sec' } else { seconds = '' }
    
    return [hours,minutes,seconds]
        .join(" ")
}

function get_one_max(tr, argument=null) {
    var tr = $( tr )
    var is_hidden = tr.hasClass('hidden')
    if (is_hidden) {
        // console.warn('max: hidden', tr)
        return []
    }
    // console.log(tr)
    var tds = tr.children()
    var label = $( tds[1] ).text().trim().toLowerCase()
    if (! label) {
        // console.warn('max: no label', label)
        return []
    }
    var values = $( tds[3] ).children()
    var quant = $( values[1] ).text().trim()
    quant = to_number(quant)
    
    // console.log(label, '<=', quant)
    return [label, quant]
}

function for_each_nav(Fn, argument=null) {
    var answer = []

    var sidetabs = $('#resourceNavParent > tbody > tr');
    $.each(sidetabs, function(index, value) {
        ob = $( value )
        // is_sidetab = ob.hasClass('sideTab');
        // if (! is_sidetab) {
        //     return;
        // }
        answer.push( Fn(ob, argument) );
    });

    return answer
}

function get_maxes() {
    var max_pairs = for_each_nav(get_one_max)
    // console.log(max_pairs)
    science_ob = $('#science')
    science_value = science_ob.text()
    science_value = to_number(science_value)
    science_max = (10 * science_value)      // actually unlimited

    fuel_ob = $('#rocketFuel')
    fuel_value = fuel_ob.text()
    fuel_value = to_number(fuel_value)
    fuel_max = (10 * fuel_value)      // actually unlimited

    rockets_max = 1_000     // NOTE: not sure how to compute this

    dark_ob = $('#stargazeNavdarkMatter_count')
    dark_value = dark_ob.text()
    dark_value = to_number(dark_value)
    dark_max = (10 * dark_value)      // actually unlimited

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
    }

    $.each(max_pairs, function(pair_idx, max_pair) {
        if (max_pair.length == 0) {
            // console.log('get_maxes: SKIP', pair_idx, max_pair)
            return
        }
        var [label, quant] = max_pair
        // console.log('get_maxes: ok', label, quant)
        maxes[label] = quant
    });
    return maxes
}

function check_tabs(maxes, available_substances) {
    const cost_flag = "Costs"
    var GLOBAL_overflow_reasons = new Object;
    var GLOBAL_pane_heading
    var GLOBAL_pane_title
    var GLOBAL_purchase
    var GLOBAL_unknown_substances
    var GLOBAL_bump_specifics
    var GLOBAL_clicked_something = false

    // console.log(panes)

    function scan_one_cost(cost_idx, cost_str) {
        if (cost_str == "") {
            // no costs (energy-mass conversion page): NOOP
            return
        }
        // console.log('cost_str:', cost_idx, cost_str)
        cost_split = cost_str
            .replaceAll(' ', '_')       // any number of spaces -> underscore
            .replace('_', ' ')          // first underscore -> space again
            .split(' ', 2);             // split on that first space
        // console.log('cost split:', cost_split)
        var [needed, substance] = cost_split
        needed = to_number(needed, cost_str)
        substance = substance.toLowerCase()
        if (substance == 'gem') { substance = 'gems' }
        known_substance = (substance in maxes)
        if (! known_substance) {
            GLOBAL_unknown_substances.push("'" + substance + "'")
            var seen = (GLOBAL_known_unknowns.includes(substance))
            if (! seen) {
                GLOBAL_known_unknowns.push(substance)
                /* if (DEBUG) */ console.warn('cost of UNKNOWN SUBSTANCE:', GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, cost_idx, '"' + cost_str + '"', substance, needed)
            }
            return
        }
        max_value = maxes[substance]
        if (needed <= max_value) {
            // console.log('cost ok:', cost_idx, substance, needed, max_value)
            return
        }

        if (GLOBAL_purchase.includes('Swarm:')) {
            console.warn('Swarm (scan_one_cost)', GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase)
            return
        }

        if (! (substance in GLOBAL_overflow_reasons)) {
            GLOBAL_overflow_reasons[substance] = []
        }
        GLOBAL_overflow_reasons[substance].push(
            GLOBAL_pane_heading + '/' + GLOBAL_pane_title + "/" + GLOBAL_purchase + ": " + from_number(needed)
        )
        GLOBAL_bump_specifics.push(substance)
    }
    
    function scan_one_tr(tr_idx, tr) {
        tr = $( tr )
        var h3 = tr.find('h3')
        GLOBAL_purchase = h3
            .text()
            .trim()
            .replace(/[/][0-9]*$/, '')  // remove "/NN" from end
            .replace(/: [0-9]*$/, '')   // remove ": NN" from end
            ;
        if (! GLOBAL_purchase) {
            return
        }
        // NOTE: delete next section:
        is_hidden = tr.hasClass('hidden')
        if (is_hidden) {
            if (DEBUG) console.warn(GLOBAL_pane_title, GLOBAL_purchase, 'HIDDEN')
            return
        }
        // NOTE: end deleted section
        if (GLOBAL_purchase.includes('Swarm:')) {
            console.warn('Swarm (scan_one_tr)', GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase)
            console.warn('tr', tr)
        }
        if (GLOBAL_pane_title == 'energy-mass conversion') {
            return
        }
        if (GLOBAL_pane_title == 'dyson swarms and sphere') {
            return
        }
        var cant_click = false
        // console.log('tr:', tr_idx, tr)
        details = tr
            .find('td > span')
            .text()
            .trim();
        var current_ob = h3
            .find('span');
        var current = current_ob
            .text()
            .trim();
        var td = tr.find('td')
        var button = td
            .find('button')
            [0];
        if (! button) {
            button = td
                .find('div.btn')
                [0];
        }
        if (button) {
            button = $( button )
        }
        if (button) {
            if (button.hasClass('destroy')) {
                console.error('destroy button!', button)
                button = null
            }
        }
        // yes, repeat the prior question
        if (button) {
            if (button.hasClass('btn-warning')) {
                button = null
            }
        }
        // yes, repeat the prior question
        if (button) {
            var button_is_hidden = button
                .hasClass('hidden');
            if (button_is_hidden) {
                // console.warn('button is hidden', button)
                button = null
            } else {
                button_is_hidden = button
                    .parent()
                    .hasClass('hidden');
                if (button_is_hidden) {
                    // console.warn('button is hidden', button.parent())
                    button = null
                }
            }
        }
        var input = td
            .find('input.desired');
        if (button && (input.length == 0)) {
            // console.warn(GLOBAL_pane_title, GLOBAL_purchase, 'Creating input object:')
            input = $('<input type="textbox" class="desired"/>')
            td.append(input)
        }
        var desired = ''
        if (input) {
            var val = input.val()
            if (val) {
                desired = val.trim()
            }
        }
        desired = to_number(desired)
        // if (current && desired) {
        //     console.log(pane_title, purchase, 'current', current, 'desired', desired)
        // }
        red_ingredients = tr
            .find('td > span span.red');
        if (red_ingredients.length) {
            // console.log('red_ingredients', red_ingredients)
            cant_click = true
        }
        DETAIL = false
        if (DEBUG) console.log('purchase:', GLOBAL_purchase)
        details = cleanup_costs(details, GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase)
        // if (DEBUG)  console.log('details:', details)
        costs = details.split(', ')     // split on "comma space"
        if (DEBUG) console.log('costs:', costs)
        if (DETAIL) console.log(GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, costs)
        GLOBAL_unknown_substances = []
        GLOBAL_bump_specifics = []
        $.each(costs, scan_one_cost)
        pop_up = []
        set_class = ''

        var all_click_classes = [
            'bump_max',
            'cant_click',
            'click_me',
            'clicking',
            'unknown_substance',
            'no_button',
        ];

        if (! button) {
            set_class = 'no_button'
        } else {
            if (desired) {
                if (! button) {
                    console.warn('Trying to click missing button', GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase)
                    cant_click = true
                }
                if (cant_click) {
                    set_class = 'cant_click'
                    pop_up.push("Missing Ingredients: " + red_ingredients.length)
                } else {
                    if (GLOBAL_clicked_something) {
                        set_class = 'click_me'
                    } else {
                        set_class = 'clicking'
                    }
                }
            }

            if (GLOBAL_bump_specifics.length) {
                set_class = 'bump_max'
                pop_up.push("Bump:")
                pop_up.push(...GLOBAL_bump_specifics)
            }
            if (GLOBAL_unknown_substances.length) {
                pop_up.push("Unknown:")
                pop_up.push(...GLOBAL_unknown_substances)
                set_class = 'unknown_substance'
            }
            if (set_class == 'clicking') {
                // if (red_ingredients.length) {
                //     console.warn('red_ingredients', red_ingredients)
                //     console.warn('cant_click:', cant_click)
                // }
                var click_time
                click_time = Math.floor(new Date().getTime() / 1000)

                var elapsed_s = (click_time - prior_cick_time)
                var TIME = toHHMMSS(elapsed_s)
                TIME = "(" + TIME.trim() + ")"
                
                button.click()
                var new_current = current_ob.text().trim();
                var VERIFY = false
                if (VERIFY && (current != '') && (new_current == current)) {
                    console.warn("ERROR: tried clicking", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, "no change", new_current, current)
                    set_class = 'click_me'
                    // need to remove click-me from removal list
                } else {
                    GLOBAL_clicked_something = true

                    console.log('AUTO-CLICK', TIME, GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, '(' + desired + ')')

                    prior_cick_time = click_time

                    desired -= 1
                    if (! desired) {
                        desired = ''
                    }
                    input.val(desired)
                }
            }
        }

        if (set_class) {
            tr.addClass(set_class)
        }
        $.each(all_click_classes, function(remove_idx, remove_me) {
            if (remove_me != set_class) {
                tr.removeClass(remove_me)
            }
        });
        if (pop_up.length) {
            reasons = pop_up
                .join("\n");
            tr.prop('title', reasons)
        } else {
            tr.prop('title', '')
        }
    }

    function scan_one_pane(pane_idx, pane) {
        pane = $(pane)
        var trs = pane.find("tr")
        var tr0 = $( trs[0] )
        var h2 = tr0.find('h2')
        GLOBAL_pane_title = h2
            .text()
            .trim()
            .toLowerCase()
            .replace(/^inside the /, '')
            .replace(/^the /, '')
            .replaceAll(' ', '_')
            ;
        known_title = (available_substances.includes(GLOBAL_pane_title))
        if (! known_title) {
            var page_designator = GLOBAL_pane_heading + '/' + GLOBAL_pane_title
            var known_skip = (GLOBAL_known_skip_page.includes(page_designator))
            if (! known_skip) {
                console.warn('Skip', page_designator)
                GLOBAL_known_skip_page.push(page_designator)
            }
            return
        }
        if (GLOBAL_pane_title == 'dyson_swarms_and_sphere') {
            // console.warn('Ignore Dyson Swarm / Sphere pane')
            return
        }
        if (DEBUG) console.log('pane:', pane)
        if (DEBUG) console.log(trs)
        if (DEBUG) console.log('tr0:', tr0)
        if (DEBUG) console.log('h2:', h2)
        if (DEBUG) console.log('pane_title:', GLOBAL_pane_title)
        $.each(trs, scan_one_tr)
    }

    var panes_ob = get_panes_ob(pane_descriptors)
    $.each(panes_ob, function(pane_heading, panes) {
        GLOBAL_pane_heading = pane_heading
        if (DEBUG) console.log('pane_heading:', GLOBAL_pane_heading)
        if (DEBUG) console.warn('panes:', pane_desc, panes)
        $.each(panes, scan_one_pane)
    });

    // console.log('overflow_reasons', GLOBAL_overflow_reasons)
    return GLOBAL_overflow_reasons
}

function cleanup_costs(orig_string, pane_heading, pane_title, purchase) {
    const cost_flag = "Costs"
    string = orig_string
    // Wonder phrases before costs:
    string = string.replace('He requires that you donate', cost_flag)
    string = string.replace('He requests a pyramid containing', cost_flag)
    string = string.replace('He requests a tower consisting of', cost_flag)
    string = string.replace('The Overlord wishes for a cube made up of', cost_flag)

    // alternate cost flag
    string = string.replace('This requires', cost_flag)
    string = string.replace('Cost:', cost_flag)

    // Wonder phrases within costs:
    string = string.replaceAll(' and ', ', ')

    // Wonder phrases after costs:
    string = string.replace(' for this knowledge', '')
    string = string.replace(' to acquire his methods', '')
    string = string.replace(' to unlock this technology', '')
    string = string.replace(' to be given this technology', '')

    // Wonder phrases to clean up:
    string = string.replace('Donate Resources', '')
    string = string.replace(/Activate .*/, '')
    string = string.replace(/Rebuild .*/, '')
    string = string.replace('Unlock Plasma Research', '')
    string = string.replace('Unlock EMC Machine Research', '')
    string = string.replace('Unlock Dyson Sphere Research', '')
    string = string.replace(/[0-9.]+%$/, '')

    // Dark Matter phrases to clean up:
    string = string.replaceAll(/Improves relationship by [0-9.]+/g, '')
    string = string.replaceAll(/Improves relationship by/g, '')

    if (pane_title == "energy-mass_conversion") {
        // does not have Costs section
        return ""
    }
    if (pane_title == 'dyson swarms and sphere') {
        // has non-standard Costs section
        return ""
    }
    // if (pane_title == "rockets") {
    //     // does not have Costs section
    //     return ""
    // }
    if (pane_title == "travel") {
        // Interstellar.
        // does not have Costs section
        return ""
    }
    if (string == '') {
        // string is now blank: no costs
        return ""
    }

    string = string.trim()

    var position = string.search(cost_flag)
    if (DEBUG) console.log('Costs Position:', position)
    if (position == -1) {
        var label = pane_heading + "/" + pane_title + "/" + purchase
        throw new Error("'Costs' not found:\n" + label + "\n'" + orig_string + "'\n---\n'" + string + "'")
    }
    position += cost_flag.length
    string = string
        .slice(position)            // delete up to after "Costs"
        .replace(/^:/, '')          // remove leading colon
        .trim()                     // remove lead/trail spaces
        .replace(/[.]+$/, '')       // remove trailing period
        .replaceAll(/  +/g, ' ')    // no doubled spaces
        ;

    // if (GLOBAL_pane_title == 'inside the wonder station') {
    //     console.log(orig_string)
    //     console.log(string)
    // }

    return string
}

function test() {

    // the following variables and functions have been copied in from check_tabs:
    var GLOBAL_overflow_reasons = new Object;
    var GLOBAL_pane_heading
    var GLOBAL_pane_title
    var GLOBAL_purchase
    var GLOBAL_unknown_substances
    var GLOBAL_bump_specifics
    var GLOBAL_clicked_something = false

    function scan_one_cost(cost_idx, cost_str) {
        if (cost_str == "") {
            // no costs (energy-mass conversion page): NOOP
            return
        }
        // console.log('cost_str:', cost_idx, cost_str)
        cost_split = cost_str
            .replaceAll(' ', '_')       // any number of spaces -> underscore
            .replace('_', ' ')          // first underscore -> space again
            .split(' ', 2);             // split on that first space
        // console.log('cost split:', cost_split)
        var [needed, substance] = cost_split
        needed = to_number(needed, cost_str)
        substance = substance.toLowerCase()
        if (substance == 'gem') { substance = 'gems' }
        known_substance = (substance in maxes)
        if (! known_substance) {
            GLOBAL_unknown_substances.push("'" + substance + "'")
            var seen = (GLOBAL_known_unknowns.includes(substance))
            if (! seen) {
                GLOBAL_known_unknowns.push(substance)
                /* if (DEBUG) */ console.warn('cost of UNKNOWN SUBSTANCE:', GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, cost_idx, '"' + cost_str + '"', substance, needed)
            }
            return
        }
        max_value = maxes[substance]
        if (needed <= max_value) {
            // console.log('cost ok:', cost_idx, substance, needed, max_value)
            return
        }

        if (GLOBAL_purchase.includes('Swarm:')) {
            console.warn('Swarm (scan_one_cost)', GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase)
            return
        }

        if (! (substance in GLOBAL_overflow_reasons)) {
            GLOBAL_overflow_reasons[substance] = []
        }
        GLOBAL_overflow_reasons[substance].push(
            GLOBAL_pane_heading + '/' + GLOBAL_pane_title + "/" + GLOBAL_purchase + ": " + from_number(needed)
        )
        GLOBAL_bump_specifics.push(substance)
    }
    
    function scan_one_tr(tr_idx, tr) {
        console.log('DEBUG s1t A tr raw', tr)
        tr = $( tr )
        console.log('DEBUG s1t B tr JQ', tr)
        var h3 = tr.find('h3')
        console.log('DEBUG s1t C h3', h3)
        GLOBAL_purchase = h3
            .text()
            .trim()
            .replace(/[/][0-9]*$/, '')  // remove "/NN" from end
            .replace(/: [0-9]*$/, '')   // remove ": NN" from end
            ;
        console.log('DEBUG s1t D h3.text', GLOBAL_purchase)
        if (! GLOBAL_purchase) {
            return
        }
        // NOTE: delete next section:
        is_hidden = tr.hasClass('hidden')
        if (is_hidden) {
            /* if (DEBUG) */ console.warn(GLOBAL_pane_title, GLOBAL_purchase, 'HIDDEN')
            return
        }
        // NOTE: end deleted section
        if (GLOBAL_purchase.includes('Swarm:')) {
            console.warn('Swarm (scan_one_tr)', GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase)
            console.warn('tr', tr)
        }
        if (GLOBAL_pane_title == 'energy-mass_conversion') {
            return
        }
        if (GLOBAL_pane_title == 'dyson swarms and sphere') {
            return
        }
        var cant_click = false
        details = tr
            .find('td > span')
            .text()
            .trim();
        // console.log('DEBUG s1t E details', details)
        var current_ob = h3
            .find('span');
        var current = current_ob
            .text()
            .trim();
        console.log('DEBUG s1t F current', current)
        var td = tr.find('td')
        var button = td
            .find('button')
            [0];
        if (! button) {
            button = td
                .find('div.btn')
                [0];
        }
        if (button) {
            button = $( button )
        }
        if (button) {
            if (button.hasClass('destroy')) {
                console.error('destroy button!', button)
                button = null
            }
        }
        // yes, repeat the prior question
        if (button) {
            if (button.hasClass('btn-warning')) {
                button = null
            }
        }
        // yes, repeat the prior question
        if (button) {
            var button_is_hidden = button
                .hasClass('hidden');
            if (button_is_hidden) {
                // console.warn('button is hidden', button)
                button = null
            } else {
                button_is_hidden = button
                    .parent()
                    .hasClass('hidden');
                if (button_is_hidden) {
                    // console.warn('button is hidden', button.parent())
                    button = null
                }
            }
        }
        console.log('DEBUG s1t G button', button)
        var input = td
            .find('input.desired');
        if (button && (input.length == 0)) {
            // console.warn(GLOBAL_pane_title, GLOBAL_purchase, 'Creating input object:')
            input = $('<input type="textbox" class="desired"/>')
            td.append(input)
        }
        var desired = ''
        if (input) {
            var val = input.val()
            if (val) {
                desired = val.trim()
            }
        }
        desired = to_number(desired)
        console.log('DEBUG s1t H desired', desired)
        // if (current && desired) {
        //     console.log(pane_title, purchase, 'current', current, 'desired', desired)
        // }
        red_ingredients = tr
            .find('td > span span.red');
        if (red_ingredients.length) {
            // console.log('red_ingredients', red_ingredients)
            cant_click = true
        }
        DETAIL = false
        if (DEBUG) console.log('purchase:', GLOBAL_purchase)
        details = cleanup_costs(details, GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase)
        // if (DEBUG)  console.log('details:', details)
        costs = details.split(', ')     // split on "comma space"
        if (DEBUG) console.log('costs:', costs)
        if (DETAIL) console.log(GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, costs)
        GLOBAL_unknown_substances = []
        GLOBAL_bump_specifics = []
        console.log('DEBUG s1t I scanning costs', costs)
        $.each(costs, scan_one_cost)
        pop_up = []
        set_class = ''

        var all_click_classes = [
            'bump_max',
            'cant_click',
            'click_me',
            'clicking',
            'unknown_substance',
            'no_button',
        ];

        if (! button) {
            set_class = 'no_button'
        } else {
            if (desired) {
                if (! button) {
                    console.warn('Trying to click missing button', GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase)
                    cant_click = true
                }
                if (cant_click) {
                    set_class = 'cant_click'
                    pop_up.push("Missing Ingredients: " + red_ingredients.length)
                } else {
                    if (GLOBAL_clicked_something) {
                        set_class = 'click_me'
                    } else {
                        set_class = 'clicking'
                    }
                }
            }

            if (GLOBAL_bump_specifics.length) {
                set_class = 'bump_max'
                pop_up.push("Bump:")
                pop_up.push(...GLOBAL_bump_specifics)
            }
            if (GLOBAL_unknown_substances.length) {
                pop_up.push("Unknown:")
                pop_up.push(...GLOBAL_unknown_substances)
                set_class = 'unknown_substance'
            }
            if (set_class == 'clicking') {
                // if (red_ingredients.length) {
                //     console.warn('red_ingredients', red_ingredients)
                //     console.warn('cant_click:', cant_click)
                // }
                var click_time
                click_time = Math.floor(new Date().getTime() / 1000)

                var elapsed_s = (click_time - prior_cick_time)
                var TIME = toHHMMSS(elapsed_s)
                TIME = "(" + TIME.trim() + ")"
                
                button.click()
                var new_current = current_ob.text().trim();
                var VERIFY = false
                if (VERIFY && (current != '') && (new_current == current)) {
                    console.warn("ERROR: tried clicking", GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, "no change", new_current, current)
                    set_class = 'click_me'
                    // need to remove click-me from removal list
                } else {
                    GLOBAL_clicked_something = true

                    console.log('AUTO-CLICK', TIME, GLOBAL_pane_heading, GLOBAL_pane_title, GLOBAL_purchase, '(' + desired + ')')

                    prior_cick_time = click_time

                    desired -= 1
                    if (! desired) {
                        desired = ''
                    }
                    input.val(desired)
                }
            }
        }

        if (set_class) {
            tr.addClass(set_class)
        }
        $.each(all_click_classes, function(remove_idx, remove_me) {
            if (remove_me != set_class) {
                tr.removeClass(remove_me)
            }
        });
        if (pop_up.length) {
            reasons = pop_up
                .join("\n");
            tr.prop('title', reasons)
        } else {
            tr.prop('title', '')
        }
    }
    // end copied section

    var maxes = get_maxes()
    var available_substances = get_available_substances(maxes)
    var panes_ob = get_panes_ob(pane_descriptors)
    // console.log('panes_ob:', panes_ob)
    var trs_ob = get_trs_ob(panes_ob, available_substances)
    console.log('trs_ob:', trs_ob)

    $.each(trs_ob, function(pane_title, trs) {
        GLOBAL_pane_heading = 'UNKNOWN'
        GLOBAL_pane_title = pane_title
        console.warn('DEBUG: each trs_ob', GLOBAL_pane_title, 'trs:', trs)
        $.each(trs, scan_one_tr)
    });
}

function jQuery_to_array(thing) {
    function filter_legal_item(line) {
        var [index, item] = line
        if (index == 'length') {
            return false
        }
        if (index == 'prevObject') {
            return false
        }
        return true
    }
    function map_second_value(line) {
        var [index, item] = line
        return item
    }
    var entries = Object.entries(thing)
    var array = entries
        .filter(filter_legal_item)
        .map(map_second_value)
        ;
    return array
}

function get_trs_ob(panes_ob, available_substances) {
    var NONLOCAL_pane_heading

    function filter_not_hidden(tr, tr_idx) {
        tr = $( tr )
        is_hidden = tr.hasClass('hidden')
        if (is_hidden) {
            return false
        }
        return true
    }

    function map_pane_to_title_and_trs(pane, pane_idx) {
        pane = $( pane )
        var trs = pane.find("tr")
        trs = jQuery_to_array(trs)
        trs = trs.filter(filter_not_hidden);
        var tr0 = trs[0]
        var tr0 = $( tr0 )
        var h2 = tr0.find('h2')
        var pane_title = h2
            .text()
            .trim()
            .toLowerCase()
            .replace(/^inside the /, '')
            .replace(/^the /, '')
            .replaceAll(' ', '_')
            ;
        var known_title = (available_substances.includes(pane_title))
        if (! known_title) {
            var page_designator = NONLOCAL_pane_heading + '/' + pane_title
            var known_skip = (GLOBAL_known_skip_page.includes(page_designator))
            if (! known_skip) {
                console.warn('Skip', page_designator)
                GLOBAL_known_skip_page.push(page_designator)
            }
            return []
        }
        // NOTE: delete this section, move logic to next function
        if (pane_title == 'dyson swarms and sphere') {
            // console.warn('Ignore Dyson Swarm / Sphere pane')
            return []
        }
        // NOTE: end deleted section

        return [pane_title, trs]
    }

    function map_panes_ob_to_all_titles_and_trs(entry) {
        var panes
        [NONLOCAL_pane_heading, panes] = entry
        var panes_array = jQuery_to_array(panes)
        var pane_data = panes_array.map(map_pane_to_title_and_trs);
        return pane_data
    }

    var panes_ob_array = Object.entries(panes_ob)
    var trs_array = panes_ob_array
        .map(map_panes_ob_to_all_titles_and_trs)
        .flat()
        ;
    trs_array = trs_array.filter(function(row) {
        return row.length > 0
    });
    var trs_ob = Object.fromEntries(trs_array)
    return trs_ob
}

function get_panes_ob(pane_descriptors) {
    pane_entries = Object.entries(pane_descriptors)

    var panes_allowed = pane_entries.filter(function(entry) {
        var [pane_heading, pane_desc] = entry
        // console.log('debug: entry', entry, 'values', pane_heading, pane_desc)

        var available = GLOBAL_tabs_available.includes(pane_heading)
        if (! available) {
            if (DEBUG) console.warn('Skip unavailable tab', pane_heading)
            return false
        }
        return true
    });
    // console.log('panes_allowed:', panes_allowed)

    var panes_array = panes_allowed.map(function(entry) {
        var [pane_heading, pane_desc] = entry
        var panes = $( pane_desc + ' .tab-pane')
        return [pane_heading, panes]
    });
    // console.log('panes_array:', panes_array)

    var panes_ob = Object.fromEntries(panes_array)
    return panes_ob
}

function colorize_one_max(tr, tab_data) {
    var tr = $( tr )
    var is_hidden = tr.hasClass('hidden')
    if (is_hidden) {
        return false
    }
    // console.log(tr)
    var tds = tr.children()
    var label = $( tds[1] )
        .text()
        .trim()
        .toLowerCase();
    is_overflow = (label in tab_data)
    if (is_overflow) {
        tr.addClass('bump_max')
        reasons = tab_data[label]
            .join("\n");
        tr.prop('title', reasons)
        return [label, 'yes']
    } else {
        tr.removeClass('bump_max')
        tr.prop('title', '')
        return [label, 'no']
    }
}

// global variable
var tick_id;

function tick() {
    // console.log('tick', tick_id)
    check_energy_levels()

    GLOBAL_tabs_available = get_tabs_available()
    // console.log('GLOBAL_tabs_available:', GLOBAL_tabs_available)
    var maxes = get_maxes()
    // console.log('maxes:', maxes)
    var available_substances = get_available_substances(maxes)
    // console.log('available_substances:', available_substances)
    GLOBAL_available_substances = available_substances
    var tab_data = check_tabs(maxes, available_substances);
    // console.log('tab_data', tab_data)
    var results = for_each_nav(colorize_one_max, tab_data)
    // console.log('results', results)
}

function tick_start() {
    var tick_milliseconds = tick_seconds * 1000
    if (tick_id) {
        tick_stop();
    }
    tick_id = setInterval(tick, tick_milliseconds)
    console.warn('tick start', tick_id)
}

function tick_stop() {
    if (tick_id) {
        clearInterval(tick_id)
        console.warn('tick stop', tick_id)
        tick_id = 0
    }
}

if (DEBUG_tick) {
    tick_stop()
    tick()
} else {
    tick_start()
}
