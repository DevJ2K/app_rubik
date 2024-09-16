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

        "d-app-bg": "#24272C",
        "d-subtle-bg": "#24272C",
        "d-ui-bg": "#24272C",
        "d-hover-ui-bg": "#24272C",
        "d-active-ui-bg": "#24272C",
        "d-subtle-border": "#24272C",
        "d-ui-border": "#24272C",
        "d-hover-ui-border": "#24272C",
        "d-accent-color": "#24272C", // "#FF5F7E",
        "d-hover-accent-color": "#24272C", // "#FF4D7A",
        "d-low-contrast-text": "#828F96",
        "d-high-contrast-text": "#E8FFFC"
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

