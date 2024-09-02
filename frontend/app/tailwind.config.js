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
        "app-bg": "#FDFDFE", // 1. App background
        "subtle-bg": "#F7F9FF", // 2. Subtle background
        "ui-bg": "#EDF2FE", // 3. UI element background
        "hover-ui-bg": "#E1E9FF", // 4. Hovered UI element background
        "active-ui-bg": "#D2DEFF", // 5. Active / Selected UI element background
        "subtle-border": "#C1D0FF", // 6. Subtle borders and separators
        "ui-border": "#ABBDF9", // 7. UI element border and focus ring
        "hover-ui-border": "#8DA4EF", // 8. Hovered UI element border
        "accent-color": "#3E63DD", // 9. Solid backgrounds
        "hover-accent-color": "#3358D4", // 10. Hovered solid backgrounds
        "low-contrast-text": "#3A5BC7", // 11. Low-contrast text
        "high-contrast-text": "#1F2D5C", // 12. High-contrast text

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

