import re
import os
import concurrent.futures


pattern_success = r'Reply from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}: bytes=\d+ time=\d+ms TTL=\d+'
comp_success = re.compile(pattern_success,re.MULTILINE)

pattern_result = r'^Ping [\w\W]+'
comp_result = re.compile(pattern_result,re.MULTILINE)

print("10.i.j.k")
b = int(input("i(1-255) = "))
c = int(input("j(1-255) = "))
d = int(input("k(1-255) = "))


def save_raw_cmd_output(ip_address):
    os.system(f'ping {ip_address} > {ip_address}.txt')
    return ip_address

def save_output_to_file(write_to_file,ip_address,results,info):
    with open(write_to_file,'a') as result:
        #writing text
        result.write(f'{ip_address} \t {bool(info)}\n')
        result.write(f'{results}\n')
    os.system(f'del {ip_address}.txt') 




for i in range(b,256):
    for j in range(c,256):
        save_raw_cmd_output(f'10.{i}.{j}.1')
        with open(f'10.{i}.{j}.1.txt','r') as f:
            text = f.read()
            #matching text
            info = re.findall(comp_success,text)
            result = re.findall(comp_result,text)

        if not info:
            save_output_to_file('dead_hosts.txt',f'10.{i}.{j}.1',result[-1],info)
            continue
        save_output_to_file('alive_hosts.txt',f'10.{i}.{j}.1',result[-1],info)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            ips = [executor.submit(save_raw_cmd_output,f'10.{i}.{j}.{k}') for k in range(d,256)]
            for ip in concurrent.futures.as_completed(ips):
                with open(f'{ip.result()}.txt','r') as f:
                    text = f.read()
                    #matching text
                    info = re.findall(comp_success,text)
                    result = re.findall(comp_result,text)
                if bool(info):
                    with open('alive_ip_list.txt','a') as f:
                        f.write(f'{ip.result()}\n')
                    save_output_to_file('result_success.txt',f'{ip.result()}',result[-1],info)
                else:
                    save_output_to_file('result_fails.txt',f'{ip.result()}',result[-1],info)