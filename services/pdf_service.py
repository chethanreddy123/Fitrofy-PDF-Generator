import asyncio
from fastapi import HTTPException
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from playwright.async_api import async_playwright

import logging


# Define a semaphore with a maximum count of 15
concurrency_semaphore = asyncio.Semaphore(15)

launch_options = {
        'headless': True,
        'args': [
            '--disable-gpu',  # Disable GPU hardware acceleration
            '--no-sandbox',   # Disable sandboxing for Linux (useful in some server environments)
            '--disable-software-rasterizer',  # Disable the software rasterizer (useful for headless mode)
            '--disable-setuid-sandbox',  # Disable setuid sandbox (useful for headless mode)
            '--disable-dev-shm-usage',  # Disable /dev/shm usage (useful for headless mode)
            '--disable-features=IsolateOrigins,site-per-process',  # Disable certain features
            '--disable-background-networking',  # Disable background network requests
            '--disable-background-timer-throttling',  # Disable background timer throttling
            '--disable-backgrounding-occluded-windows',  # Disable backgrounding of occluded windows
            '--disable-breakpad',  # Disable crash reports
            '--disable-client-side-phishing-detection',  # Disable client-side phishing detection
            '--disable-features=IsolateOrigins',  # Additional disabling of certain features
            '--disable-site-isolation-trials',  # Disable site isolation trials
            '--autoplay-policy=user-gesture-required',  # Require user gesture for autoplay policy
            '--disable-background-networking',  # Disable background networking
            '--disable-background-timer-throttling',  # Disable background timer throttling
            '--disable-backgrounding-occluded-windows',  # Disable backgrounding of occluded windows
            '--disable-breakpad',  # Disable crash reports
            '--disable-client-side-phishing-detection',  # Disable client-side phishing detection
            '--disable-component-update',  # Disable component update
            '--disable-default-apps',  # Disable default apps
            '--disable-dev-shm-usage',  # Disable /dev/shm usage
            '--disable-domain-reliability',  # Disable domain reliability
            '--disable-extensions',  # Disable extensions
            '--disable-features=AudioServiceOutOfProcess',  # Disable certain audio service features
            '--disable-hang-monitor',  # Disable hang monitor
            '--disable-ipc-flooding-protection',  # Disable IPC flooding protection
            '--disable-notifications',  # Disable notifications
            '--disable-offer-store-unmasked-wallet-cards',  # Disable offer store unmasked wallet cards
            '--disable-popup-blocking',  # Disable popup blocking
            '--disable-print-preview',  # Disable print preview
            '--disable-prompt-on-repost',  # Disable prompt on repost
            '--disable-renderer-backgrounding',  # Disable renderer backgrounding
            '--disable-setuid-sandbox',  # Disable setuid  sandbox
            '--disable-speech-api',  # Disable speech API
            '--disable-sync',  # Disable sync
            '--hide-scrollbars',  # Hide scrollbars
            '--ignore-gpu-blacklist',  # Ignore GPU blacklist
            '--metrics-recording-only',  # Record metrics only
            '--mute-audio',  # Mute audio
            '--no-default-browser-check',  # No default browser check
            '--no-first-run',  # No first run
            '--no-pings',  # No pings
            '--no-zygote',  # No zygote
            '--password-store=basic',  # Use basic password store
            '--use-gl=swiftshader',  # Use SwiftShader for WebGL
            '--use-mock-keychain'  # Use mock keychain
        ]

    }


class PDFServiceV2:
    @staticmethod
    def render_html(template_path: str, data: dict) -> str:
        template_loader = FileSystemLoader(searchpath=str(Path.cwd()  / 'templates'))
        template_env = Environment(loader=template_loader)
        template = template_env.get_template(template_path)
        return template.render(data)

    @staticmethod
    # async def generate_pdf_from_html2(html_content: str) -> bytes:
    #     try:
    #         async with async_playwright() as p:
    #             browser = await p.chromium.launch(**launch_options)
                
    #             context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.21 Safari/537.36")
                
    #             page = await context.new_page()
                
    #             await page.set_content(html_content)

    #             # waiting for all images to load
    #             await page.wait_for_selector('img')
  

    #             await page.emulate_media(media="print")
                
    #             pdf_data = await page.pdf(format='A4')

    #             return pdf_data
    #     except Exception as e:
    #         logging.error(f"Error generating PDF: {str(e)}")
    #         raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")
    #     finally:
    #         if 'browser' in locals():
    #             await browser.close()
                
    async def generate_pdf_from_html2(html_content: str) -> bytes:
        try:
            async with concurrency_semaphore:
                async with async_playwright() as p:
                    browser = await p.chromium.launch(**launch_options)
                    context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.21 Safari/537.36")

                    page = await context.new_page()

                    await page.set_content(html_content)

                    pdf_data = await page.pdf(format='A4')

            return pdf_data 
        except Exception as e:
            logging.error(f"Error generating PDF: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")
        finally:
            if 'browser' in locals():
                await browser.close()