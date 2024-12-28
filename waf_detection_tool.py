#By: Jey Zeta
import requests
import re
import sys
import os
from utils.banner import generar_banner, mostrar_ayuda_completa
from termcolor import colored
import emoji

VERSION = "1.0.0"

def detectar_waf(url):

    waf_signatures = {
        "Cloudflare": ["cloudflare"],
        "Akamai": ["akamai"],
        "Barracuda": ["barracuda"],
        "F5 BIG-IP": ["f5", "big-ip"],
        "Sucuri": ["sucuri"],
        "Fortinet": ["fortinet", "fortigate"],
        "Imperva Incapsula": ["incapsula", "imperva"],
        "Citrix NetScaler": ["netscaler", "citrix"],
        "AWS WAF": ["awselb", "aws"],
        "StackPath": ["stackpath"],
        "DenyAll": ["denyall"],
        "Jiasule": ["jiasule"],
        "Wallarm": ["wallarm"],
        "AliyunDun": ["aliyun"],
        "ModSecurity": ["modsecurity", "mod_sec"],
        "Reblaze": ["reblaze"],
        "Varnish": ["varnish"],
        "Palo Alto Networks": ["palo alto", "pan-os"],
        "Wordfence": ["wordfence"],
        "SiteLock": ["sitelock"],
        "Imunify360": ["imunify360"],
        "360WangZhanBao": ["360wzb"],
        "Sucuri CloudProxy": ["sucuri"],
        "Yundun": ["yundun"],
        "Zenedge": ["zenedge"],
        "ZScaler": ["zscaler"],
        "Airlock": ["airlock"],
        "RSFirewall": ["rsfirewall"],
        "SiteGuard": ["siteguard"],
        "WebKnight": ["webknight"],
        "BulletProof Security Pro": ["bulletproof"],
        "NinjaFirewall": ["ninjafirewall"],
        "F5 TrafficShield": ["trafficshield"],
        "Fastly": ["fastly"],
        "Azure Front Door": ["azure"],
        "Big-IP AppSec Manager": ["f5 asm"],
        "PerimeterX": ["perimeterx"]
    }

    try:
        response = requests.get(url, timeout=10)
        headers = response.headers

        for waf_name, patterns in waf_signatures.items():
            for pattern in patterns:
                if any(re.search(pattern, str(value), re.IGNORECASE) for value in headers.values()):
                    return colored(f"WAF detectado: {waf_name}", "green")

        waf_keywords = [
            "access denied", "web application firewall", "403 forbidden", "406 not acceptable",
            "security violation", "blocked by", "firewall"
        ]
        if any(re.search(keyword, response.text, re.IGNORECASE) for keyword in waf_keywords):
            return colored("WAF detectado en el contenido de la respuesta.", "green")

        return colored("No se detectó un WAF.", "green")

    except requests.RequestException as e:
        return colored(f"Error al realizar la solicitud: {e}", "red")

def mostrar_version():
    print(generar_banner()) 
    print(colored(f"Versión de la herramienta: {VERSION}", "green"))

def mostrar_lista_wafs():
    waf_list = [
        "Cloudflare", "Akamai", "Barracuda", "F5 BIG-IP", "Sucuri", "Fortinet", "Imperva Incapsula",
        "Citrix NetScaler", "AWS WAF", "StackPath", "DenyAll", "Jiasule", "Wallarm", "AliyunDun",
        "ModSecurity", "Reblaze", "Varnish", "Palo Alto Networks", "Wordfence", "SiteLock",
        "Imunify360", "360WangZhanBao", "Sucuri CloudProxy", "Yundun", "Zenedge", "ZScaler",
        "Airlock", "RSFirewall", "SiteGuard", "WebKnight", "BulletProof Security Pro",
        "NinjaFirewall", "F5 TrafficShield", "Fastly", "Azure Front Door", "Big-IP AppSec Manager",
        "PerimeterX"
    ]
    print(generar_banner())  
    print(colored("WAFs soportados:", "green"))
    
    fire_emoji = "\033[1;35m🔥\033[0m"  # Código ANSI para el emoji de fuego en color púrpura

    for waf in waf_list:
        print(f"{fire_emoji} {waf}")

if __name__ == "__main__":
    os.system("printf '\033]2;WAF dt v1.0.0 🧱\\a'")
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "-l":
            mostrar_lista_wafs()
        elif sys.argv[1] == "-h":
            mostrar_ayuda_completa()
        elif sys.argv[1] == "-v":
            mostrar_version()
        else:
            print(generar_banner())
            url = sys.argv[1]
            print(detectar_waf(url))
    else:
        mostrar_ayuda_completa()
