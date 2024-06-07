import requests
import time

def testconn(ipcip):

    content1="正在播放:\n假装我是歌名"
    content2="HW useage"
    headers={
        "Accept": "*/*",
        "Accept-Language": "zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.5, en; q=0.2",
        "Authorization": "Basic YWRtaW46NzM1NTYwOFlDWHljeC4=",
        "Cache-Control": "no-cache",
        "Connection": "Keep-Alive",
        "Content-Type": "text/plain; charset=UTF-8",
        "Cookie": "userInfo=YWRtaW46NzM1NTYwOFlDWHljeC4%3D; lang_type=en-us; rememberPWD=true; ocxVersion=2%2C1%2C1%2C3; auInfo=YWRtaW46NzM1NTYwOFlDWHljeC4%3D; profile_count=3; whMode=0%3A0",
        "If-Modified-Since": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    }

    info=f'''
        <config xmlns="http://www.ipc.com/ver10" version="1.7">
        <types>
        <dateFormat>
        <enum>year-month-day</enum>
        <enum>month-day-year</enum>
        <enum>day-month-year</enum>
        </dateFormat>
        <osdOverlayType>
        <enum>TEXT</enum>
        <enum>IMAGE</enum>
        </osdOverlayType>
        </types>
        <imageOsd>
        <time>
        <switch type="boolean">true</switch>
        <X type="uint32">6600</X>
        <Y type="uint32">200</Y>
        <dateFormat type="dateFormat">year-month-day</dateFormat>
        </time>
        <channelName>
        <switch type="boolean">false</switch>
        <X type="uint32">75</X>
        <Y type="uint32">100</Y>
        <name type="string" maxLen="18"><![CDATA[IPC]]></name>
        </channelName>
        <textOverLay type="list" count="4">
        <item>
        <switch type="boolean">false</switch>
        <X type="uint32">75</X>
        <Y type="uint32">900</Y>
        <value type="string" maxLen="15"></value>
        <showLevel type="uint32">0</showLevel>
        <flickerSwitch type="boolean">false</flickerSwitch>
        <osdOverlayType type="osdOverlayType">TEXT</osdOverlayType>
        </item>
        <item>
        <switch type="boolean">true</switch>
        <X type="uint32">750</X>
        <Y type="uint32">8100</Y>
        <value type="string" maxLen="32"><![CDATA[{content1}]]></value>
        <showLevel type="uint32">0</showLevel>
        <flickerSwitch type="boolean">false</flickerSwitch>
        <osdOverlayType type="osdOverlayType">TEXT</osdOverlayType>
        </item>
        <item>
        <switch type="boolean">true</switch>
        <X type="uint32">800</X>
        <Y type="uint32">1100</Y>
        <value type="string" maxLen="15"><![CDATA[{content2}]]></value>
        <showLevel type="uint32">0</showLevel>
        <flickerSwitch type="boolean">false</flickerSwitch>
        <osdOverlayType type="osdOverlayType">TEXT</osdOverlayType>
        </item>
        <item>
        <switch type="boolean">false</switch>
        <X type="uint32">75</X>
        <Y type="uint32">4800</Y>
        <value type="string" maxLen="15"></value>
        <showLevel type="uint32">0</showLevel>
        <flickerSwitch type="boolean">false</flickerSwitch>
        <osdOverlayType type="osdOverlayType">TEXT</osdOverlayType>
        </item>
        </textOverLay>
        </imageOsd>
        </config>
    '''
    url=f"http://{ipcip}/SetImageOsdConfig"
    try:
        response = requests.post(url, data=info.encode("utf-8"), headers=headers,verify=False)
        return response.status_code,"fine"
    except Exception as e:
        return "ERR",e

def uosd(ipcip,content1,content2):
    headers={
        "Accept": "*/*",
        "Accept-Language": "zh-Hans-CN, zh-Hans; q=0.8, en-US; q=0.5, en; q=0.2",
        "Authorization": "Basic YWRtaW46NzM1NTYwOFlDWHljeC4=",
        "Cache-Control": "no-cache",
        "Connection": "Keep-Alive",
        "Content-Type": "text/plain; charset=UTF-8",
        "Cookie": "userInfo=YWRtaW46NzM1NTYwOFlDWHljeC4%3D; lang_type=en-us; rememberPWD=true; ocxVersion=2%2C1%2C1%2C3; auInfo=YWRtaW46NzM1NTYwOFlDWHljeC4%3D; profile_count=3; whMode=0%3A0",
        "If-Modified-Since": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
    }

    info=f'''
        <config xmlns="http://www.ipc.com/ver10" version="1.7">
        <types>
        <dateFormat>
        <enum>year-month-day</enum>
        <enum>month-day-year</enum>
        <enum>day-month-year</enum>
        </dateFormat>
        <osdOverlayType>
        <enum>TEXT</enum>
        <enum>IMAGE</enum>
        </osdOverlayType>
        </types>
        <imageOsd>
        <time>
        <switch type="boolean">true</switch>
        <X type="uint32">6600</X>
        <Y type="uint32">200</Y>
        <dateFormat type="dateFormat">year-month-day</dateFormat>
        </time>
        <channelName>
        <switch type="boolean">false</switch>
        <X type="uint32">75</X>
        <Y type="uint32">100</Y>
        <name type="string" maxLen="18"><![CDATA[IPC]]></name>
        </channelName>
        <textOverLay type="list" count="4">
        <item>
        <switch type="boolean">false</switch>
        <X type="uint32">75</X>
        <Y type="uint32">900</Y>
        <value type="string" maxLen="15"></value>
        <showLevel type="uint32">0</showLevel>
        <flickerSwitch type="boolean">false</flickerSwitch>
        <osdOverlayType type="osdOverlayType">TEXT</osdOverlayType>
        </item>
        <item>
        <switch type="boolean">true</switch>
        <X type="uint32">750</X>
        <Y type="uint32">8100</Y>
        <value type="string" maxLen="32"><![CDATA[{content1}]]></value>
        <showLevel type="uint32">0</showLevel>
        <flickerSwitch type="boolean">false</flickerSwitch>
        <osdOverlayType type="osdOverlayType">TEXT</osdOverlayType>
        </item>
        <item>
        <switch type="boolean">true</switch>
        <X type="uint32">800</X>
        <Y type="uint32">1100</Y>
        <value type="string" maxLen="15"><![CDATA[{content2}]]></value>
        <showLevel type="uint32">0</showLevel>
        <flickerSwitch type="boolean">false</flickerSwitch>
        <osdOverlayType type="osdOverlayType">TEXT</osdOverlayType>
        </item>
        <item>
        <switch type="boolean">false</switch>
        <X type="uint32">75</X>
        <Y type="uint32">4800</Y>
        <value type="string" maxLen="15"></value>
        <showLevel type="uint32">0</showLevel>
        <flickerSwitch type="boolean">false</flickerSwitch>
        <osdOverlayType type="osdOverlayType">TEXT</osdOverlayType>
        </item>
        </textOverLay>
        </imageOsd>
        </config>
    '''
    url=f"http://{ipcip}/SetImageOsdConfig"

    response = requests.post(url, data=info.encode("utf-8"), headers=headers,verify=False)

    return response.status_code

if __name__ == '__main__':
    print(uosd("192.168.0.201","正在播放:\n无限无线无限无限无限无限无限无","CPU"))
    #total=15
    #for i in range(total):
    #    print(uosd("192.168.0.201",f"正在播放:\n["+"="*i+" "*(total-i-1)+"]"))
    #    time.sleep(1)