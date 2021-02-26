from selenium import webdriver

# URLs being scraped -

url = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
url2 = "https://proxy-daily.com/"
url3 = "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"

# Driver -

driver = webdriver.Chrome()

ans = str(input("Do you want to clear the previous lists? (Y/N) : ")).lower()

if ans in ('y', 'yes', 'ok', 'ye'):
    print("Clearing any existing lists...")
    http = open("https.txt", 'w')
    socks4 = open("socks4.txt", 'w')
    socks5 = open("socks5.txt", 'w')
    http.write('')
    socks4.write('')
    socks5.write('')
    print("Done")

    # Source 1 - HTTP

    print("Scraping source 1...")
    driver.get(url)
    src1_elementtext = driver.find_element_by_xpath('/html/body/pre')
    src1_save = open("https.txt", "a")
    src1_save.write(src1_elementtext.text)
    src1_save.write("\n")
    src1_save.close()
    print("Done")

    # Source 2 - HTTP/S/SSL,Socks :

    print("Scraping source 2...")
    driver.get(url2)

    src2_http = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]")
    src2_http_save = open("https.txt", "a")
    src2_http_save.write(src2_http.text)
    src2_http_save.write("\n")
    src2_http_save.close()

    src2_socks4 = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]")
    src2_socks4_save = open("socks4.txt", "a")
    src2_socks4_save.write(src2_socks4.text)
    src2_socks4_save.write("\n")
    src2_socks4_save.close()

    src2_socks5 = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[6]")
    src2_socks5_save = open("socks5.txt", "a")
    src2_socks5_save.write(src2_socks5.text)
    src2_socks5_save.write("\n")
    src2_socks5_save.close()

    print("Done")

    # Source 3 - HTTP/S/SSL,Socks :

    print("Scraping source 3...")
    driver.get(url3)
    src3_socks5 = driver.find_element_by_xpath("/html/body/pre")
    src3_socks5_save = open("socks5.txt", 'a')
    src3_socks5_save.write(src3_socks5.text)
    src3_socks5_save.write("\n")
    src3_socks5_save.close()

    print("Done")

elif ans in ['n', 'no', 'nop', 'nope']:
    # Source 1 - HTTP

    print("Scraping source 1...")
    driver.get(url)
    src1_elementtext = driver.find_element_by_xpath('/html/body/pre')
    src1_save = open("https.txt", "a")
    src1_save.write(src1_elementtext.text)
    src1_save.write("\n")
    src1_save.close()
    print("Done")

    # Source 2 - HTTP/S/SSL,Socks :

    print("Scraping source 2...")
    driver.get(url2)

    src2_http = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]")
    src2_http_save = open("https.txt", "a")
    src2_http_save.write(src2_http.text)
    src2_http_save.write("\n")
    src2_http_save.close()

    src2_socks4 = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[4]")
    src2_socks4_save = open("socks4.txt", "a")
    src2_socks4_save.write(src2_socks4.text)
    src2_socks4_save.write("\n")
    src2_socks4_save.close()

    src2_socks5 = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[6]")
    src2_socks5_save = open("socks5.txt", "a")
    src2_socks5_save.write(src2_socks5.text)
    src2_socks5_save.write("\n")
    src2_socks5_save.close()

    print("Done")

    # Source 3 - HTTP/S/SSL,Socks :

    print("Scraping source 3...")
    driver.get(url3)
    src3_socks5 = driver.find_element_by_xpath("/html/body/pre")
    src3_socks5_save = open("socks5.txt", 'a')
    src3_socks5_save.write(src3_socks5.text)
    src3_socks5_save.write("\n")
    src3_socks5_save.close()

    print("Done")
else:
    print("Invalid response!")

