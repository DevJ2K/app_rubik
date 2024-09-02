/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: "class",
  theme: {
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
      // b_project_card: "930px"
    },
    extend: {
      colors: {

        // "app-bg": "#FEECFF", // 1. App background
        // "subtle-bg": "#FEEFFF", // 2. Subtle background
        // "ui-bg": "#FDEAFF", // 3. UI element background
        // "hover-ui-bg": "#F8DAFB", // 4. Hovered UI element background
        // "active-ui-bg": "#FCDEFF", // 5. Active / Selected UI element background
        // "subtle-border": "#FBC7FF", // 6. Subtle borders and separators
        // "ui-border": "#FAB6FF", // 7. UI element border and focus ring
        // "hover-ui-border": "#F897FF", // 8. Hovered UI element border
        // "accent-color": "#EC64F4", // 9. Solid backgrounds
        // "hover-accent-color": "#DC40E5", // 10. Hovered solid backgrounds
        // "low-contrast-text": "#83008A", // 11. Low-contrast text
        // "high-contrast-text": "#5B0060", // 12. High-contrast text
        "app-bg": "#F9FEFF", // 1. App background
        "subtle-bg": "#F1FAFD", // 2. Subtle background
        "ui-bg": "#E1F6FD", // 3. UI element background
        "hover-ui-bg": "#D1F0FA", // 4. Hovered UI element background
        "active-ui-bg": "#BEE7F5", // 5. Active / Selected UI element background
        "subtle-border": "#A9DAED", // 6. Subtle borders and separators
        "ui-border": "#8DCAE3", // 7. UI element border and focus ring
        "hover-ui-border": "#60B3D7", // 8. Hovered UI element border
        "accent-color": "#7CE2FE", // 9. Solid backgrounds
        "hover-accent-color": "#74DAF8", // 10. Hovered solid backgrounds
        "low-contrast-text": "#00749E", // 11. Low-contrast text
        "high-contrast-text": "#1D3E56", // 12. High-contrast text

        "d-app-bg": "#0B032D",
        "d-subtle-bg": "#1E0F45",
        "d-ui-bg": "#2B155D",
        "d-hover-ui-bg": "#371B6D",
        "d-active-ui-bg": "#441F7D",
        "d-subtle-border": "#532E91",
        "d-ui-border": "#6A3DB1",
        "d-hover-ui-border": "#8546D4",
        "d-accent-color": "#EC64F4", // "#FF5F7E",
        "d-hover-accent-color": "#DC40E5", // "#FF4D7A",
        "d-low-contrast-text": "#FFD1DC",
        "d-high-contrast-text": "#FFE4F1"
      }


    },
    fontFamily: {
      Poppins: ["Poppins, sans-serif"],
    },
    container: {
      marginLeft: "auto",
      marginRight: "auto",
      width: "100%",
      padding: "2rem",
      center: true,
      screens: {
        'sm': '100%',
        'md': '100%',
        'lg': '1100px', // 48rem
        'xl': '1100px'
      }
    }
  },
  variants: {
    extend: {
      backgroundColor: ['dark'],
    },
  },
  plugins: [],
}

