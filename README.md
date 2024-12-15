# WebScraper - A Webpage Downloader and Resource Recreator

**WebScraper** is an intuitive web scraping and resource management tool that allows users to download and save webpage content along with associated resources. It enables the recreation of webpages from previously saved content, providing a seamless way to store and access important resources for web development and other educational purposes.

## Features & Capabilities

### **1. Webpage Downloading & Resource Saving**
- **HTML Content Downloading:** The platform allows users to enter the URL of a webpage, scrape its HTML content, and download it along with its associated resources (images, scripts, stylesheets, etc.).
- **Resource Handling:** The tool handles the downloading of all associated resources (like images, scripts, etc.) and stores them locally in the appropriate folder structure.
- **Automatic Saving:** Resources are automatically saved to a designated folder with properly sanitized filenames to avoid conflicts.

### **2. Webpage Recreation**
- **Recreate Saved Webpages:** Users can easily recreate any previously downloaded webpage by simply selecting it from the list of available saved pages. The tool opens the `index.html` file in the default web browser, giving the user access to the complete saved webpage.
- **Saved Webpages List:** A list of previously downloaded and saved webpages is displayed, allowing users to easily navigate and select the page they wish to view again.

### **3. Resource Management**
- **Download External Resources:** The WebScraper intelligently detects external resources referenced in the HTML (like CSS, JavaScript, and image files) and downloads them locally, adjusting the webpage’s HTML to point to the local resources.
- **Cross-Platform Resource Handling:** The tool ensures that all file paths are platform-independent, supporting both Windows and Unix-like systems.

### **4. User-Friendly Interface**
- **Simple GUI:** The tool uses a user-friendly graphical interface built with `customtkinter`, providing buttons for key actions like generating a new webpage download or recreating a previously saved webpage.
- **Dynamic Debugging:** The interface includes a dynamic text area for displaying status messages and error logs, keeping the user informed about the progress of downloads and page recreation.

### **5. File Location Management**
- **Configurable File Location:** Users can specify and manage the location where webpages and resources are saved. This feature ensures flexibility for storing content in desired directories.

### **6. Headless Web Scraping**
- **Web Scraping with Selenium:** The tool uses Selenium for headless browsing, meaning it can scrape dynamic web pages (e.g., those that rely on JavaScript) without opening a full browser window. This makes it highly efficient and quick for real-time use.
- **Automated Data Handling:** The tool automates the downloading of resources and updating of HTML to match the local file structure.

### **7. Error Handling and Debugging**
- **Detailed Error Messages:** If an error occurs during resource download or page recreation, the platform displays specific error messages to guide the user through troubleshooting.
- **Progress Tracking:** The system tracks the progress of resource downloading, displaying a percentage of completed downloads and a log of any issues encountered.

## How It Works
1. **Download Webpage:** Enter a URL and click "Generate" to scrape the webpage and download its content along with any associated resources.
2. **Recreate Webpage:** If you wish to view a previously downloaded webpage, select it from the list and click "Recreate" to open it in your default web browser.
3. **Manage Resources:** All resources (images, stylesheets, scripts) are saved locally, and the HTML is updated to reference these resources, ensuring the webpage works offline.

## Technologies Used
- **Frontend:** CustomTkinter (for GUI), Python (for logic and scripting)
- **Web Scraping:** Selenium (for dynamic content scraping), Requests (for static content download)
- **HTML Parsing:** BeautifulSoup (for parsing and modifying HTML content)
- **File Management:** OS, shutil (for handling file paths and managing downloads)

## Conclusion
WebScraper is a powerful tool for web developers, students, or anyone who needs to download and store webpages and their associated resources. Whether for offline access or educational purposes, this tool simplifies the process of saving and recreating webpages, with a clean and efficient user interface.
