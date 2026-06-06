# Space Company Automation Project

Automation script and UI enhancements for the idle game [Space Company](https://sparticle999.github.io/SpaceCompany/).

## Project Structure

- `space_company_js_inject.js`: The main automation logic. Uses jQuery to parse the game's DOM and automate resource management and purchases.
- `space_company_js_inject.css`: Styling for the injected UI elements and visual feedback (e.g., highlighting items that need attention).
- `setup_node_v20.sh`: Environment setup script for Node.js (used for development tools or local testing).

## Terms of Art

The following terms are used throughout the codebase to describe game elements:

- **Category**: The main navigation tabs at the top of the page (Resources, Solar System, etc.).
- **Item**: The entities listed in the left sidebar under a Category (Metal, Gems, Science Production, etc.).
- **Page**: The main content area on the right that appears when an Item is clicked.
- **Clack**: Individual purchase/action buttons within a Page (e.g., "Gain 1", "Miner", "Storage Upgrade").
- **Substance**: A resource or entity tracked by the automation script.

## Coding Conventions

- **Libraries**: Relies heavily on **jQuery** (accessed via `$`).
- **Formatting**: Adheres to JSLint standards. See file headers for specific JSLint flags.
- **Naming**: 
  - `clean_name`: A normalized version of a name used for internal logic and mapping.
  - `pane_title`: The identifier for a specific UI section or resource page.
- **Modularity**: Logic is organized into parsing (`get_quantities`), analysis (`update_clack_fields`), and action (`compose_clack_object`) phases.

## Visual Indicators (CSS)

The injected CSS provides status feedback:
- **Red Border**: Energy deficit.
- **Orange Border**: Falling energy levels.
- **Light Green**: Item is ready for purchase ("Click Me").
- **Pink**: Resource storage limit reached ("Bump Max").
- **Yellow/Orange**: High cost or high resource rate required.

## Development & Debugging

- Use the `DEBUG` and `DEBUG_tick` flags in `space_company_js_inject.js` to toggle verbose logging.
- The `TEST` flag can be used to run logic without executing game actions.
- Avoid modifying the "Destroy" buttons unless explicitly instructed, as they are intentionally styled for safety.
