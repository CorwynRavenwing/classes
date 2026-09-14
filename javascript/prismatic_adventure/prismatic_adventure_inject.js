// prismatic_adventure_inject.js

// Control variables to toggle auto-restart behavior
var default_config = {
    autoRestartEnergy: true,
    autoRestartCopium: true,
    automate: 'OFF',    // allowed values: 'zone', 'all', 'OFF'
    taskMode: 'OFF'     // Options: 'OFF', 'Normal', 'Travel', 'ALL'
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

var HUD_VERSION = '1.4';

/**
 * Injects a floating HUD control panel into the page.
 */
function createHUD() {
    'use strict';
    // Prevent duplicate HUD creation
    var existingHud = document.getElementById('jsbot-hud');

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
    hud.id = 'jsbot-hud';
    hud.setAttribute('data-version', HUD_VERSION);

    // Apply floating panel styling directly via inline CSS
    hud.style.cssText =
            'position: fixed;' +
            'top: 300px;' +
            'right: 50px;' +
            'z-index: 999999;' +
            'background: rgba(20, 20, 25, 0.92);' +
            'color: #e0e0e0;' +
            'border: 1px solid #444;' +
            'border-radius: 8px;' +
            'padding: 12px 16px;' +
            'font-family: monospace;' +
            'font-size: 12px;' +
            'box-shadow: 0 4px 12px rgba(0,0,0,0.5);' +
            'user-select: none;' +
            'min-width: 200px;';

    hud.innerHTML =
            '<div style="display: flex; justify-content: space-between; align-items: center; font-weight: bold; font-size: 13px; margin-bottom: 10px; color: #4af; border-bottom: 1px solid #333; padding-bottom: 4px;">' +
            '    <span>JS Bot Control</span>' +
            '    <span style="font-size: 10px; color: #888;">v' + HUD_VERSION + '</span>' +
            '</div>' +
            '<div style="display: flex; flex-direction: column; gap: 8px;">' +
            '    <label style="display: flex; align-items: center; justify-content: space-between; cursor: pointer;">' +
            '        <span>Restart Energy:</span>' +
            '        <input type="checkbox" id="hud-energy">' +
            '    </label>' +
            '    <label style="display: flex; align-items: center; justify-content: space-between; cursor: pointer;">' +
            '        <span>Restart Copium:</span>' +
            '        <input type="checkbox" id="hud-copium">' +
            '    </label>' +
            '    <label style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">' +
            '        <span>Task Mode:</span>' +
            '        <select id="hud-task-mode" style="background: #222; color: #fff; border: 1px solid #555; padding: 2px 4px; border-radius: 4px;">' +
            '            <option value="OFF">OFF</option>' +
            '            <option value="Normal">Normal</option>' +
            '            <option value="Travel">Travel</option>' +
            '            <option value="ALL">ALL</option>' +
            '        </select>' +
            '    </label>' +
            '    <label style="display: flex; align-items: center; justify-content: space-between; gap: 8px;">' +
            '        <span>Automation:</span>' +
            '        <select id="hud-automate" style="background: #222; color: #fff; border: 1px solid #555; padding: 2px 4px; border-radius: 4px;">' +
            '            <option value="OFF">OFF</option>' +
            '            <option value="zone">Zone</option>' +
            '            <option value="all">All</option>' +
            '        </select>' +
            '    </label>' +
            '    <div style="display: flex; justify-content: space-between; border-top: 1px solid #333; padding-top: 6px; margin-top: 2px;">' +
            '        <span>Max Energy:</span>' +
            '        <span id="hud-max-energy" style="color: #4f4; font-weight: bold;">--</span>' +
            '    </div>' +
            '</div>';

    document.body.appendChild(hud);

    // Sync initial state from config after appending
    var energyCheckbox = document.getElementById('hud-energy');
    var copiumCheckbox = document.getElementById('hud-copium');
    var automateSelect = document.getElementById('hud-automate');
    var taskModeSelect = document.getElementById('hud-task-mode');

    if (energyCheckbox) {
        energyCheckbox.checked = config.autoRestartEnergy;
    }
    if (copiumCheckbox) {
        copiumCheckbox.checked = config.autoRestartCopium;
    }
    if (automateSelect) {
        automateSelect.value = config.automate;
    }
    if (taskModeSelect) {
        taskModeSelect.value = config.taskMode;
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

// Global variable to store the timer reference
var botIntervalId = null;

/**
 * Main execution tick.
 * Calls all modular checks sequentially.
 */
function run() {
    'use strict';

    // Always run per-tick visual syncs
    updateHUDStats();
    syncTaskCheckboxes();

    // Execute first successful action and short-circuit remainder
    return (
        checkAndRestartEnergy()
        || checkAndRestartCopium()
        || setZoneAutomation()
        || processAutomatedTasks()
        // Future modular checks can be added here
    );
}

/**
 * Starts the heartbeat timer.
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

/**
 * Stops the heartbeat timer.
 */
function stopBot() {
    'use strict';
    if (botIntervalId !== null) {
        clearInterval(botIntervalId);
        botIntervalId = null;
        console.log('[JS Bot] Heartbeat stopped.');
    }
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
