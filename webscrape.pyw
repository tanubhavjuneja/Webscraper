import os
import time
import requests
import sys
import customtkinter as ctk
from PIL import Image
from urllib.parse import urljoin, unquote, urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webbrowser
import tkfilebrowser
def recreation():
    webpage_list = get_webpage_list()
    if webpage_list:
        list_window = ctk.CTkToplevel()
        list_window.overrideredirect(True)
        list_window.geometry("360x250+1190+390")
        web_frame = ctk.CTkScrollableFrame(list_window, height=240, width=350)
        web_frame.pack(fill="both", expand=True)
        for webpage in webpage_list:
            webpage_button = ctk.CTkButton(web_frame, text=webpage, command=lambda wb=webpage: recreate_selected_webpage(wb, list_window))
            webpage_button.pack(pady=5, padx=10, fill="x")
    else:
        display("No webpages available to recreate.")
def recreate_selected_webpage(selected_webpage, list_window):
    selected_webpage_path = os.path.join(mfl, "webpages", selected_webpage)
    recreate_webpage(selected_webpage_path)
    list_window.destroy()
def recreate_webpage(selected_webpage_path):
    try:
        webbrowser.open(os.path.join(selected_webpage_path, "index.html"), new=2)
        display(f"Webpage recreated. Opening index.html in the default web browser.")
    except Exception as e:
        display(f"Error: {e}. Unable to open the webpage. Try recreating it first.")
def get_webpage_list():
    webpages_folder = os.path.join(mfl, "webpages")
    if os.path.exists(webpages_folder) and os.path.isdir(webpages_folder):
        webpage_list = [item for item in os.listdir(webpages_folder) if os.path.isdir(os.path.join(webpages_folder, item))]
        return webpage_list
    return []
def display(msg):
    debug_frame.configure(state=ctk.NORMAL)
    debug_frame.insert('end', msg + '\n')
    debug_frame.see('end')
    debug_frame.configure(state=ctk.DISABLED)
def is_inline_data_url(url):
    return url.startswith('data:')
def sanitize_filename(url):
    if is_inline_data_url(url):
        content_type, _ = url.split(';')
        _, extension = content_type.split('/')
        filename = f"inline_data.{extension}"
    else:
        filename = ''.join(c if c.isalnum() or c in {'_', '.'} else '_' for c in unquote(url))
        filename = filename[:255]
    return filename
def download_and_save_resource(base_url, resource_url, output_folder, count):
    full_url = urljoin(base_url, resource_url)
    try:
        response = requests.get(full_url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        display(f"Error downloading resource {full_url}: {e}")
        return None
    filename = sanitize_filename(full_url)
    output_folder = output_folder.rstrip(os.path.sep)  
    resource_path = os.path.join(output_folder, filename)
    os.makedirs(os.path.dirname(resource_path), exist_ok=True)
    with open(resource_path, 'wb') as file:
        file.write(response.content)
    display(f"Resource saved: {resource_path}")
    count['downloaded'] += 1
    return os.path.relpath(resource_path, output_folder).replace("\\", "/")
def get_html_with_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        time.sleep(2)
        return driver.page_source
    finally:
        driver.quit()
def main1():
    base_url = webfield.get("0.0", "end").rstrip()
    domain_name = urlparse(base_url).hostname
    output_folder = os.path.join(mfl, "webpages/", domain_name)
    os.makedirs(output_folder, exist_ok=True)
    try:
        html_content = get_html_with_selenium(base_url)
        if html_content:
            soup = BeautifulSoup(html_content, 'html.parser')
            resource_tags = soup.find_all(['link', 'script', 'img'])
            total_resources = len(resource_tags)
            count = {'downloaded': 0}
            for tag in resource_tags:
                resource_url = tag.get('href') or tag.get('src')
                if resource_url:
                    local_file_path = download_and_save_resource(base_url, resource_url, output_folder, count)
                    if local_file_path:
                        tag['href'] = tag['src'] = local_file_path
            html_output_path = os.path.join(output_folder, "index.html")
            with open(html_output_path, 'w', encoding='utf-8') as html_file:
                html_file.write(str(soup))
            display(f"HTML content and resources saved to {html_output_path}")
            percentage_recreated = (count['downloaded']/ total_resources) * 100
            display(f"Successfully read {percentage_recreated:.2f}% of the webpage.")
        else:
            display(f"Failed to retrieve content from {base_url}")
    except Exception as e:
        display(f"Error: {e}. Enter a valid URL.")
def close():
    main.destroy()
    sys.exit()
def read_file_location():
    global mfl
    try:
        file=open('web_location.txt', 'r')
        mfl = file.read().strip()
        file.close()
        if not os.path.isfile(os.path.join(mfl, 'icons/close.png')):
            get_file_location()
    except FileNotFoundError:
        get_file_location()
def get_file_location():
    global main
    main=ctk.CTk()
    main.geometry("200x50+860+420")
    main.attributes('-topmost', True)
    main.attributes("-alpha",100.0)
    main.lift()
    file_button = ctk.CTkButton(main, text="Select File Location",command=select_file_location,width=1)
    file_button.pack(pady=10)
    main.mainloop()
def select_file_location():
    global main
    mfl = str(tkfilebrowser.askopendirname())+"/"
    mfl = mfl.replace('\\', '/')
    file=open('web_location.txt', 'w')
    file.write(mfl)
    file.close()
    main.destroy()
    read_file_location()
read_file_location()
main=ctk.CTk()
main.geometry("440x250+740+390")
main.overrideredirect(True)
main.attributes("-alpha",100.0)
main.lift()
title=ctk.CTkLabel(main,text="Webscraper",font=("Arial",20,"bold"),bg_color="gray14",fg_color="gray14",text_color="DarkOrchid2")
title.place(rely=0.02,relx=0.38)
close_icon = ctk.CTkImage(Image.open(mfl+"icons/close.png"), size=(15, 15))
close_button = ctk.CTkButton(main, image=close_icon, command=close,text="",width=1,fg_color="gray14")
close_button.place(relx=0.925,rely=0.01)
webname=ctk.CTkLabel(main,text="Enter Webpage URL :",font=("Arial",15,"bold"),bg_color="gray14",fg_color="gray14")
webname.place(relx=0.03,rely=0.18)
webfield=ctk.CTkTextbox(main,height=25,width=250,wrap=ctk.WORD)
webfield.bind("<Return>", lambda e: "break")
webfield.place(relx=0.39,rely=0.18)
generate=ctk.CTkButton(main,command=main1,text="Generate",font=("Arial",15,"bold"),fg_color="DarkOrchid3")
generate.place(rely=0.35,relx=0.15)
recreate=ctk.CTkButton(main,command=recreation,text="Recreate",font=("Arial",15,"bold"),fg_color="DarkOrchid3")
recreate.place(rely=0.35,relx=0.55)
debug_frame = ctk.CTkTextbox(main, width=412, height=100,font=("Arial",12,"bold"),text_color="limegreen",fg_color="gray10", state=ctk.DISABLED)
debug_frame.place(relx=0.03,rely=0.54)
main.mainloop()