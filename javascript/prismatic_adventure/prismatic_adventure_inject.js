// prismatic_adventure_inject.js

// Global variable to store the timer reference
var botIntervalId = null;

/**
 * Stops the heartbeat timer.
 * startBot is much lower down, so it can call other functions
 */
function stopBot() {
    'use strict';
    if (botIntervalId !== null) {
        clearInterval(botIntervalId);
        botIntervalId = null;
        console.log('[JS Bot] Heartbeat stopped.');
    }
}
// Control variables to toggle auto-restart behavior
var default_config = {
    autoRestartEnergy: true,
    autoRestartCopium: true,
    automate: 'OFF',    // allowed values: 'zone', 'all', 'OFF'
    taskMode: 'OFF',    // Options: 'OFF', 'Normal', 'Travel', 'ALL'
    autoResources: true
};

var config;
if (!config) {
    config = default_config;
}

// Control variables for which items' checkboxes are checked
// Keys will be "zoneIdx_taskIdx", e.g., "4_8": true
var taskAutoStore;
if (!taskAutoStore) {
    taskAutoStore = {};
}

var resourceAutoStore;
if (!resourceAutoStore) {
    resourceAutoStore = {};
}

/**
 * Checks if an element is missing, hidden via CSS class, inline display, or visually detached.
 * @param {HTMLElement|string} target - The DOM element or string ID to check.
 * @returns {boolean} - True if hidden or missing, False if visible.
 */
function isElementHidden(target) {
    'use strict';

    const el = (
        (typeof target === 'string')
            ? document.getElementById(target)
            : target
    );

    if (!el) {
        return true;
    }

    return (
        el.classList.contains('hidden')
        || el.style.display === 'none'
        || el.offsetParent === null
    );
}

var HUD_VERSION = '1.5';

/**
 * Injects a floating HUD control panel into the page.
 */
function createHUD() {
    'use strict';
    // Prevent duplicate HUD creation
    var existingHud_A = document.getElementById('jsbot-hud');
    var existingHud_B = document.getElementById('prismatic-bot-hud');
    var existingHud = existingHud_A || existingHud_B;

    if (existingHud) {
        var oldVersion = existingHud.getAttribute('data-version') || 'unknown';

        // Check if existing HUD version matches current version
        if (oldVersion === HUD_VERSION) {
            return;
        }
        // Remove outdated HUD instance to force re-render
        console.log('[JS Bot] Replacing obsolete HUD version ' + oldVersion + ' -> ' + HUD_VERSION);
        existingHud.parentNode.removeChild(existingHud);
    }

    var hud = document.createElement('div');
    hud.id = 'prismatic-bot-hud';
    hud.setAttribute('data-version', HUD_VERSION);

    hud.innerHTML =
            '<div class="hud-header">' +
            '    <span>Prismatic Bot</span>' +
            '    <span class="hud-version">v' + HUD_VERSION + '</span>' +
            '</div>' +

            // 1. Clearing Zone Controls
            '<fieldset class="hud-zone-group" id="hud-group-clearing">' +
            '    <legend>Clearing Zone Controls</legend>' +
            '    <div class="hud-row disabled-row">' +
            '        <span>Automation:</span>' +
            '        <span class="hud-disabled-tag">N/A (Clearing)</span>' +
            '    </div>' +
            '    <div class="hud-row">' +
            '        <label><span>Clearing Tasks:</span>' +
            '            <select id="hud-task-mode-clearing">' +
            '                <option value="OFF">OFF</option>' +
            '            <option value="Normal">Normal</option>' +
            '            <option value="Travel">Travel</option>' +
            '            <option value="ALL">ALL</option>' +
            '        </select>' +
            '    </label>' +
            '    </div>' +
            '</fieldset>' +

            // 2. Automatable Zone Controls
            '<fieldset class="hud-zone-group" id="hud-group-automatable">' +
            '    <legend>Automated Zone Controls</legend>' +
            '    <div class="hud-row">' +
            '        <label><span>Automation:</span>' +
            '            <select id="hud-automate">' +
            '            <option value="OFF">OFF</option>' +
            '            <option value="zone">Zone</option>' +
            '            <option value="all">All</option>' +
            '                <option value="manual">Manual</option>' +
            '            </select>' +
            '        </label>' +
            '    </div>' +

            '    <div class="hud-row">' +
            '        <label><span>Auto Tasks:</span>' +
            '            <select id="hud-task-mode-auto">' +
            '                <option value="OFF">OFF</option>' +
            '                <option value="Normal">Normal</option>' +
            '                <option value="Travel">Travel</option>' +
            '                <option value="ALL">ALL</option>' +
            '            </select>' +
            '        </label>' +
            '    </div>' +
            '</fieldset>' +

            '<div class="hud-stats-group">' +
            '    <div class="hud-row">' +
            '        <label for="hud-auto-resources">' +
            '            <span>Use Resources:</span>' +
            '            <input type="checkbox" id="hud-auto-resources">' +
            '        </label>' +
            '    </div>' +
            '    <div class="hud-stat-row">' +
            '        <span>Max Energy:</span>' +
            '        <span id="hud-max-energy" class="hud-stat-value">--</span>' +
            '    </div>' +
            '</div>' +

    if (energyCheckbox) {
            '<fieldset class="game-over-group">' +
            '    <legend>Game Over Restarts</legend>' +
            '    <div class="hud-row">' +
            '        <label><span>Restart Energy:</span><input type="checkbox" id="hud-auto-restart-energy"></label>' +
            '    </div>' +
            '    <div class="hud-row">' +
            '        <label><span>Restart Copium:</span><input type="checkbox" id="hud-auto-restart-copium"></label>' +
            '    </div>' +
            '    <div class="hud-row">' +
            '        <label><span>Restart Delusion:</span><input type="checkbox" id="hud-auto-restart-delusion"></label>' +
            '    </div>' +
            '</fieldset>';

    return hud;
}
    if (automateSelect) {
        automateSelect.value = config.automate;
    }
    if (taskModeSelect) {
        taskModeSelect.value = config.taskMode;
    }

    if (autoResourcesCheckbox) {
        autoResourcesCheckbox.checked = config.autoResources;
        autoResourcesCheckbox.addEventListener('change', function (e) {
            config.autoResources = e.target.checked;
            console.log('[JS Bot] Use Resources set to: ' + config.autoResources);
        });
    }

    // Bind controls using standard function callbacks
    if (energyCheckbox) {
        energyCheckbox.addEventListener('change', function (e) {
            config.autoRestartEnergy = e.target.checked;
            console.log('[JS Bot] Auto Restart Energy set to: ' + config.autoRestartEnergy);
        });
    }

    if (copiumCheckbox) {
        copiumCheckbox.addEventListener('change', function (e) {
            config.autoRestartCopium = e.target.checked;
            console.log('[JS Bot] Auto Restart Copium set to: ' + config.autoRestartCopium);
        });
    }

    if (automateSelect) {
        automateSelect.addEventListener('change', function (e) {
            config.automate = e.target.value;
            console.log('[JS Bot] Automation mode set to: ' + config.automate);
        });
    }

    if (taskModeSelect) {
        taskModeSelect.addEventListener('change', function (e) {
            config.taskMode = e.target.value;
            console.log('[JS Bot] Task Mode set to: ' + config.taskMode);
        });
    }
}

/**
 * Decorates a single task element with an auto-run checkbox.
 * @param {Element} taskEl - The DOM element representing the task.
 */
function decorateTaskElement(taskEl) {
    'use strict';

    var zoneIdx = taskEl.getAttribute('data-zone-index');
    var taskIdx = taskEl.getAttribute('data-task-index');

    if (zoneIdx === null || taskIdx === null) {
        return;
    }

    var taskKey = zoneIdx + '_' + taskIdx;

    // Check if checkbox control already exists
    if (taskEl.querySelector('.jsbot-task-checkbox')) {
        return;
    }

    var computedView = document.defaultView || taskEl.ownerDocument.defaultView;
    if (computedView && computedView.getComputedStyle(taskEl).position === 'static') {
        taskEl.style.position = 'relative';
    }

    var label = document.createElement('label');
    label.className = 'jsbot-task-label';
    label.style.cssText =
            'position: absolute;' +
            'top: 4px;' +
            'right: 6px;' +
            'z-index: 100;' +
            'font-size: 10px;' +
            'color: #4af;' +
            'background: rgba(0,0,0,0.6);' +
            'padding: 1px 4px;' +
            'border-radius: 3px;' +
            'cursor: pointer;' +
            'user-select: none;';

    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'jsbot-task-checkbox';
    checkbox.style.cssText = 'margin-right: 3px; vertical-align: middle;';

    // Restore previous stored state if it exists
    if (taskAutoStore[taskKey] === true) {
        checkbox.checked = true;
    }
    checkbox.addEventListener('change', function (e) {
        taskAutoStore[taskKey] = e.target.checked;
        console.log('[JS Bot] Task [' + taskKey + '] auto-run set to: ' + e.target.checked);
    });

    label.appendChild(checkbox);
    label.appendChild(document.createTextNode('auto'));
    taskEl.appendChild(label);
}

/**
 * Scans for tasks in the DOM and injects/syncs auto-run checkboxes.
 */
function syncTaskCheckboxes() {
    'use strict';

    var tasks = document.querySelectorAll('#tasks .task');

    Array.prototype.forEach.call(tasks, function (taskEl) {
        decorateTaskElement(taskEl);
    });
}

/**
 * Decorates a single resource DOM element with an auto-consume checkbox.
 * @param {Element} resEl - The resource element.
 */
function decorateResourceElement(resEl) {
    'use strict';

    // Identify resource by data attribute, id, or fallback
    var resKey = (
        resEl.getAttribute('data-resource')
        || resEl.getAttribute('data-name')
        || resEl.id
    );

    if (!resKey) {
        return;
    }

    if (resEl.querySelector('.jsbot-resource-checkbox')) {
        return;
    }

    var computedView = document.defaultView || resEl.ownerDocument.defaultView;
    if (computedView && computedView.getComputedStyle(resEl).position === 'static') {
        resEl.style.position = 'relative';
    }

    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'jsbot-resource-checkbox';
    checkbox.style.cssText =
            'position: absolute;' +
            'top: 2px;' +
            'right: 2px;' +
            'z-index: 100;' +
            'cursor: pointer;' +
            'margin: 0;';

    if (resourceAutoStore[resKey] === true) {
        checkbox.checked = true;
    }

    checkbox.addEventListener('change', function (e) {
        resourceAutoStore[resKey] = e.target.checked;
        console.log('[JS Bot] Resource [' + resKey + '] auto-consume set to: ' + e.target.checked);
    });

    // Prevent clicking the checkbox from triggering the underlying resource click
    checkbox.addEventListener('click', function (e) {
        e.stopPropagation();
    });

    resEl.appendChild(checkbox);
}

/**
 * Scans for resource elements in the DOM and injects auto-consume checkboxes.
 */
function syncResourceCheckboxes() {
    'use strict';

    var resources = document.querySelectorAll('#resourcesGrid .resource-item, #resources .resource-item, .resource-node');

    Array.prototype.forEach.call(resources, function (resEl) {
        decorateResourceElement(resEl);
    });
}

/**
 * Dispatches a synthetic contextmenu (right-click) event to a target DOM node.
 * Uses strict dynamic references to satisfy global-variable linters.
 * @param {Element} element - The target DOM element.
 */
function triggerRightClick(element) {
    'use strict';

    if (!element || !element.ownerDocument) {
        return;
    }

    var doc = element.ownerDocument;
    var return_this = function () {
        return this;
    };
    var view = doc.defaultView || return_this();
    var evt;

    if (view && typeof view.MouseEvent === 'function') {
        evt = new view.MouseEvent('contextmenu', {
            bubbles: true,
            cancelable: true,
            view: view,
            button: 2,
            buttons: 2
        });
    } else if (doc.createEvent) {
        evt = doc.createEvent('MouseEvents');
        evt.initMouseEvent(
            'contextmenu',
            true,   // bubbles
            true,   // cancelable
            view,   // view
            1,      // detail
            0,      // screenX
            0,      // screenY
            0,      // clientX
            0,      // clientY
            false,  // ctrl
            false,  // alt
            false,  // shift
            false,  // meta
            2,      // button (right click)
            null    // relatedTarget
        );
    }

    if (evt) {
        element.dispatchEvent(evt);
    }
}

/**
 * Predicate to determine if a resource is executable.
 * @param {Element} resEl - The resource element.
 * @returns {boolean} True if eligible to be consumed.
 */
function isResourceExecutable(resEl) {
    'use strict';

    if (!config.autoResources || isElementHidden(resEl)) {
        return false;
    }

    var resKey = (
        resEl.getAttribute('data-resource')
        || resEl.getAttribute('data-name')
        || resEl.id
    );

    if (!resKey || resourceAutoStore[resKey] !== true) {
        return false;
    }

    return true;
}

/**
 * Automates right-clicking checked, available resources.
 * @returns {boolean} True if a resource was right-clicked, false otherwise.
 */
function processAutomatedResources() {
    'use strict';

    if (!config.autoResources) {
        return false;
    }

    var resources = document.querySelectorAll('#resourcesGrid .resource-item, #resources .resource-item, .resource-node');
    var executableResources = Array.prototype.filter.call(resources, isResourceExecutable);

    if (executableResources.length === 0) {
        return false;
    }

    var targetRes = executableResources[0];
    var resKey = (
        targetRes.getAttribute('data-resource')
        || targetRes.getAttribute('data-name')
        || targetRes.id
    );

    triggerRightClick(targetRes);
    console.log('[JS Bot] Right-clicked automated resource [' + resKey + ']');
    return true;
}

/**
 * Determines whether a task element is a zone travel task.
 * @param {Element} taskEl - The task element to check.
 * @returns {boolean} True if it is a travel task, false otherwise.
 */
function isTravelTask(taskEl) {
    'use strict';
    return taskEl.classList.contains('travel-task');
}

/**
 * Helper predicate: determines if a task element is eligible to be automated.
 * @param {Element} taskEl - The task element to evaluate.
 * @returns {boolean} True if the task is eligible under current taskMode, false otherwise.
 */
function isTaskExecutable(taskEl) {
    'use strict';

    var mode = config.taskMode;

    // Master switch OFF
    if (mode === 'OFF') {
        return false;
    }

    var travel = isTravelTask(taskEl);

    // Normal mode: reject travel tasks
    if (mode === 'Normal' && travel) {
        return false;
    }

    // Travel mode: reject normal (non-travel) tasks
    if (mode === 'Travel' && !travel) {
        return false;
    }

    if (isElementHidden(taskEl)) {
        return false;
    }

    var zoneIdx = taskEl.getAttribute('data-zone-index');
    var taskIdx = taskEl.getAttribute('data-task-index');

    if (zoneIdx === null || taskIdx === null) {
        return false;
    }

    var taskKey = zoneIdx + '_' + taskIdx;

    if (taskAutoStore[taskKey] !== true) {
        return false;
    }

    var button = taskEl.querySelector('.task-control button');
    if (!button || button.classList.contains('active') || button.disabled) {
        return false;
    }

    return true;
}

/**
 * Automates execution for checked, available tasks.
 * @returns {boolean} True if a task button was clicked, false otherwise.
 */
function processAutomatedTasks() {
    'use strict';

    var tasks = document.querySelectorAll('#tasks .task');

    // Filter down to only valid, clickable task elements
    var executableTasks = Array.prototype.filter.call(tasks, isTaskExecutable);

    if (executableTasks.length === 0) {
        return false;
    }

    // Sort clickable tasks: regular tasks come before travel tasks
    executableTasks.sort(function (a, b) {
        var aIsTravel = isTravelTask(a);
        var bIsTravel = isTravelTask(b);

        if (aIsTravel && !bIsTravel) {
            return 1;  // Move travel task 'a' to the end
        }
        if (!aIsTravel && bIsTravel) {
            return -1; // Keep regular task 'a' ahead of travel task 'b'
        }
        return 0;      // Preserve original DOM order for identical types
    });

    var targetTask = executableTasks[0];
    var zoneIdx = targetTask.getAttribute('data-zone-index');
    var taskIdx = targetTask.getAttribute('data-task-index');
    var button = targetTask.querySelector('.task-control button');

    button.click();
    console.log('[JS Bot] Executing automated task [' + zoneIdx + '_' + taskIdx + ']');
    return true;
}

/**
 * Helper function to check visibility, click a button, and log output.
 * @param {string} containerId - The ID of the container element to check.
 * @param {string} buttonId - The ID of the restart button to click.
 * @param {boolean} isEnabled - The control variable enabling this check.
 * @param {string} logMessage - Message to log upon clicking.
 * @returns {boolean} - True if clicked, False otherwise.
 */
function handleAutoRestart(containerId, buttonId, isEnabled, logMessage) {
    'use strict';

    if (!isEnabled) {
        return false;
    }

    const container = document.getElementById(containerId);
    if (!container) {
        return false;
    }

    // Check if hidden via inline style or CSS class
    const isHidden = isElementHidden(container);

    if (isHidden) {
        return false;
    }

    const restartBtn = document.getElementById(buttonId);

    if (!restartBtn) {
        return false;
    }

    restartBtn.click();
    console.log(`[JS Bot] ${logMessage}`);

    return true;
}

// Function 1: Check & Restart for Energy Game Over
function checkAndRestartEnergy() {
    'use strict';

    return handleAutoRestart(
        'gameOverContentEnergy',
        'restartButtonEnergy',
        config.autoRestartEnergy,
        'Energy Game Over detected. Clicking Restart.'
    );
}

// Function 2: Check & Restart for Copium Game Over
function checkAndRestartCopium() {
    'use strict';

    return handleAutoRestart(
        'gameOverContentCopium',
        'restartButtonCopium',
        config.autoRestartCopium,
        'Copium Game Over detected. Clicking Restart.'
    );
}

/**
 * Ensures the specified automation button is active if present.
 * @returns {boolean} - True if an action was taken, False if target state was already met or elements missing.
 */
function setZoneAutomation() {
    'use strict';
    var container = document.getElementById('zoneAutomation');

    // Guard clause: check container existence and visibility
    if (isElementHidden(container)) {
        return false;
    }

    var zoneBtn = container.querySelector('button[data-automation="zone"]');
    var allBtn = container.querySelector('button[data-automation="all"]');

    // Guard clause: confirm buttons exist
    if (!zoneBtn || !allBtn) {
        return false;
    }

    var targetMode = config.automate;

    if (targetMode === 'zone' && !zoneBtn.classList.contains('active')) {
        zoneBtn.click();
        console.log('[JS Bot] Set automation to: Zone');
        return true;
    }

    if (targetMode === 'all' && !allBtn.classList.contains('active')) {
        allBtn.click();
        console.log('[JS Bot] Set automation to: All');
        return true;
    }

    if (targetMode === 'OFF') {
        if (zoneBtn.classList.contains('active')) {
            zoneBtn.click();
            console.log('[JS Bot] Disabled Zone automation');
            return true;
        }
        if (allBtn.classList.contains('active')) {
            allBtn.click();
            console.log('[JS Bot] Disabled All automation');
            return true;
        }
    }

    return false; // No action needed/taken
}

/**
 * Reads the energy bar tooltip and returns the maximum energy capacity.
 * @returns {number|null} Max energy capacity, or null if missing/unparseable.
 */
function getMaxEnergy() {
    'use strict';
    var energyBar = document.getElementById('energyBar');
    if (isElementHidden(energyBar)) {
        return null;
    }

    var tooltip = energyBar.getAttribute('data-tooltip');
    if (!tooltip) {
        return null;
    }

    // Matches "Energy: 50.9/287" -> captures "287"
    var match = tooltip.match(/Energy:\s*[\d.]+\/([\d.]+)/);
    if (match && match[1]) {
        return parseFloat(match[1]);
    }

    return null;
}

/**
 * Updates the read-only Max Energy value in the HUD.
 */
function updateHUDStats() {
    'use strict';
    var maxEnergy = getMaxEnergy();
    var displayEl = document.getElementById('hud-max-energy');

    if (displayEl) {
        displayEl.textContent = (
            (maxEnergy !== null)
                ? maxEnergy
                : '--'
        );
    }
}

/**
 * Main execution tick.
 * Calls all modular checks sequentially.
 */
function run() {
    'use strict';

    // Always run per-tick visual syncs
    updateHUDStats();
    syncTaskCheckboxes();
    syncResourceCheckboxes();

    // Execute first successful action and short-circuit remainder
    return (
        checkAndRestartEnergy()
        || checkAndRestartCopium()
        || processAutomatedResources()
        || setZoneAutomation()
        || processAutomatedTasks()
        // Future modular checks can be added here
    );
}

/**
 * Starts the heartbeat timer.
 * stopBot is much higher up, so other functions can call it
 * @param {number} intervalMs - Milliseconds between ticks (default: 1000).
 */
function startBot(intervalMs) {
    'use strict';
    // Clear any existing timer to prevent running duplicate loops
    if (botIntervalId !== null) {
        clearInterval(botIntervalId);
    }

    botIntervalId = setInterval(run, intervalMs);
    console.log(`[JS Bot] Heartbeat started (${intervalMs}ms interval).`);
}

// Initialize HUD and start heartbeat loop on script injection
createHUD();
startBot(1000);

function dont_complain() {
    'use strict';
    // run();
    stopBot();
    dont_complain();
}
