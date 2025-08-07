from .data import (
    APP_NAME,
    APP_NAME_CAP,
    NOTIF_POS_DEFAULT,
    NOTIF_POS_KEY,
    PANEL_POSITION_DEFAULT,
    PANEL_POSITION_KEY,
    WALLPAPERS_DIR_DEFAULT,
)

SOURCE_STRING = f"""
# {APP_NAME_CAP}
source = ~/.config/{APP_NAME_CAP}/config/hypr/{APP_NAME}.conf
"""

DEFAULTS = {
    "hotkeys": {
        "restart": {
            "prefix": "SUPER ALT",
            "suffix": "B",
            "enabled": True
        },
        "dash": {
            "prefix": "SUPER",
            "suffix": "W",
            "enabled": True
        },
        "bluetooth": {
            "prefix": "SUPER",
            "suffix": "Y",
            "enabled": False
        },
        "pins": {
            "prefix": "SUPER",
            "suffix": "Q",
            "enabled": False
        },
        "kanban": {
            "prefix": "SUPER",
            "suffix": "N",
            "enabled": True
        },
        "launcher": {
            "prefix": "SUPER",
            "suffix": "TAB",
            "enabled": True
        },
        "tmux": {
            "prefix": "SUPER",
            "suffix": "T",
            "enabled": False
        },
        "cliphist": {
            "prefix": "SUPER",
            "suffix": "B",
            "enabled": True
        },
        "toolbox": {
            "prefix": "SUPER",
            "suffix": "F",
            "enabled": True
        },
        "overview": {
            "prefix": "SUPER",
            "suffix": "O",
            "enabled": True
        },
        "wallpapers": {
            "prefix": "SUPER",
            "suffix": "COMMA",
            "enabled": True
        },
        "randwall": {
            "prefix": "SUPER SHIFT",
            "suffix": "COMMA",
            "enabled": False
        },
        "mixer": {
            "prefix": "SUPER",
            "suffix": "L",
            "enabled": True
        },
        "emoji": {
            "prefix": "SUPER",
            "suffix": "PERIOD",
            "enabled": True
        },
        "power": {
            "prefix": "SUPER",
            "suffix": "ESCAPE",
            "enabled": True
        },
        "caffeine": {
            "prefix": "SUPER SHIFT",
            "suffix": "C",
            "enabled": False
        },
        "css": {
            "prefix": "SUPER SHIFT",
            "suffix": "B",
            "enabled": True
        },
        "inspector": {
            "prefix": "SUPER CTRL ALT",
            "suffix": "B",
            "enabled": False
        }
    },
    "wallpapers_dir": WALLPAPERS_DIR_DEFAULT,
    "bar_position": "Top",  # New default position setting
    "vertical": False,  # Kept for backward compatibility
    "centered_bar": False,
    "datetime_12h_format": False,  # Add this line
    "terminal_command": "kitty -e",
    "dock_enabled": True,
    "dock_icon_size": 28,
    "dock_always_occluded": False,
    "bar_workspace_show_number": False,
    "bar_workspace_use_chinese_numerals": False,
    "bar_hide_special_workspace": True,  # Toggle (Hide/Show) special workspace
    "bar_theme": "Pills",
    "dock_theme": "Pills",
    "panel_theme": "Notch",  # Default panel theme
    PANEL_POSITION_KEY: PANEL_POSITION_DEFAULT,  # Default panel position
    NOTIF_POS_KEY: NOTIF_POS_DEFAULT,  # Nueva entrada para la posición de notificaciones
    "bar_button_apps_visible": True,
    "bar_systray_visible": True,
    "bar_control_visible": True,
    "bar_network_visible": True,
    "bar_button_tools_visible": True,
    "bar_sysprofiles_visible": True,
    "bar_button_overview_visible": True,
    "bar_ws_container_visible": True,
    "bar_weather_visible": True,
    "bar_battery_visible": True,
    "bar_metrics_visible": True,
    "bar_language_visible": True,
    "bar_date_time_visible": True,
    "bar_button_power_visible": True,
    "corners_visible": True,
    "bar_metrics_disks": ["/"],
    "metrics_visible": {
        "cpu": True,
        "ram": True,
        "disk": True,
        "gpu": True,
    },
    "metrics_small_visible": {
        "cpu": True,
        "ram": True,
        "disk": True,
        "gpu": True,
    },
    "limited_apps_history": ["Spotify"],
    "history_ignored_apps": ["Hyprshot"],
}
