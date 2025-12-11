// Chart Theme Customization System

export const CHART_THEMES = {
  default: {
    name: "Default (Professional Blue)",
    colors: {
      usRate: "#667eea",
      chinaRate: "#e74c3c",
      usOnChina: "#f39c12",
      chinaOnUs: "#9b59b6",
      gridStroke: "#f0f0f0",
      axisStroke: "#999",
      tooltip: "#fff",
      tooltipBorder: "#ccc"
    },
    description: "Professional blue and red theme"
  },
  
  ocean: {
    name: "Ocean Wave",
    colors: {
      usRate: "#0077be",
      chinaRate: "#ff6b6b",
      usOnChina: "#00d4ff",
      chinaOnUs: "#ffa500",
      gridStroke: "#e3f2fd",
      axisStroke: "#5c7caf",
      tooltip: "#f8f9fa",
      tooltipBorder: "#0077be"
    },
    description: "Cool ocean tones"
  },
  
  sunset: {
    name: "Sunset Glow",
    colors: {
      usRate: "#ff6b35",
      chinaRate: "#f7931e",
      usOnChina: "#fdc830",
      chinaOnUs: "#c13c0a",
      gridStroke: "#ffe5c3",
      axisStroke: "#d9480f",
      tooltip: "#fffef5",
      tooltipBorder: "#ff6b35"
    },
    description: "Warm sunset colors"
  },
  
  forest: {
    name: "Forest Green",
    colors: {
      usRate: "#2d6a4f",
      chinaRate: "#d62828",
      usOnChina: "#52b788",
      chinaOnUs: "#a4161a",
      gridStroke: "#d8f3dc",
      axisStroke: "#40916c",
      tooltip: "#f1faee",
      tooltipBorder: "#2d6a4f"
    },
    description: "Natural green tones"
  },
  
  midnight: {
    name: "Midnight Dark",
    colors: {
      usRate: "#64dfdf",
      chinaRate: "#ff6b9d",
      usOnChina: "#c06c84",
      chinaOnUs: "#f67280",
      gridStroke: "#2a2a3e",
      axisStroke: "#888",
      tooltip: "#1a1a2e",
      tooltipBorder: "#64dfdf"
    },
    description: "Dark mode theme"
  },
  
  vibrant: {
    name: "Vibrant Pop",
    colors: {
      usRate: "#aa96da",
      chinaRate: "#fcbad3",
      usOnChina: "#ffffd2",
      chinaOnUs: "#b4e7ff",
      gridStroke: "#f5f5f5",
      axisStroke: "#999",
      tooltip: "#fff",
      tooltipBorder: "#aa96da"
    },
    description: "Bright and playful"
  },

  neutral: {
    name: "Neutral Grayscale",
    colors: {
      usRate: "#4a4a4a",
      chinaRate: "#757575",
      usOnChina: "#999999",
      chinaOnUs: "#bdbdbd",
      gridStroke: "#e0e0e0",
      axisStroke: "#666",
      tooltip: "#fff",
      tooltipBorder: "#999"
    },
    description: "Professional grayscale"
  },

  corporate: {
    name: "Corporate Blue",
    colors: {
      usRate: "#003f5c",
      chinaRate: "#d32f2f",
      usOnChina: "#fbc02d",
      chinaOnUs: "#c2185b",
      gridStroke: "#e3f2fd",
      axisStroke: "#1565c0",
      tooltip: "#eceff1",
      tooltipBorder: "#003f5c"
    },
    description: "Corporate standard theme"
  }
};

export const getTheme = (themeName) => {
  return CHART_THEMES[themeName] || CHART_THEMES.default;
};

export const getThemeNames = () => {
  return Object.keys(CHART_THEMES);
};

export const getThemeOptions = () => {
  return Object.entries(CHART_THEMES).map(([key, value]) => ({
    value: key,
    label: value.name,
    description: value.description
  }));
};

export const applyThemeToChart = (theme) => {
  return {
    strokeWidth: 3,
    dotRadius: 4,
    gridStrokeDasharray: "3 3",
    colors: theme.colors
  };
};
