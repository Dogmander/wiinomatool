print("Wii no Ma Tool 0.5 Beta")
import datetime
import os
def generate_events(info):
    '''
    generate_events -> str
    Returns the XML for today.xml.
    Arguments:
    info (dict): A dictionary with the required info. I need to look into today.xml
    Returns:
    str: What should be in today.xml
    '''
    
    raise NotImplementedError('I need to look into today.xml')
class FirstBinTemplate:
    '''
    This class contains info about first.bin
    Attributes:
    ver (int): first.bin version
    eula (int): EULA version
    url1 (str): See first.txt
    url2 (str): See first.txt
    url3 (str): See first.txt
    '''
    def __init__(self,ver=399,eula=3,url1='http://66.61.72.125/url1/',url2='http://66.61.72.125/url2/',url3='http://66.61.72.125/url3/'):
        
        self.ver = ver
        print(self.ver)
        self.eula = eula
        self.url1 = url1
        self.url2 = url2
        self.url3 = url3
        self.firstbin = '''
<Config>
  <ver>{}</ver>
  <maint>0</maint>
  <url1>{}</url1>
  <url2>{}</url2>
  <url3>{}</url3>
  <eulaver>{}</eulaver>
  <shopurl>http://66.61.72.125/shopurl/index.esf</shopurl>
  <shopkey>7fce738e542f0a60fe5d8d8e1e8781af</shopkey>
  <shopvalid>1</shopvalid>
  <akahost>5</akahost>
  <akaca>1</akaca>
  <smpkey>5ab362aa57dbb1dc16849e3e2d1cf2ff</smpkey>
  <fmax>30</fmax>
  <bmax>10</bmax>
  <upddt>{}</upddt>
</Config>
        '''


    def is_ver_valid(self):
        '''
        is_ver_valid -> str
        Checks if the version is valid
        '''
        if self.ver == 9999:
            return 'Invalid Discontinuted'
    def gen_firstbin(self):
        '''
        gen_firstbin -> None
        Creates a first.bin in the current directory
        '''
        print(self.ver)
        fornoma = '%Y-%d-%mT%H:%M:%S'
        time = datetime.datetime.now().strftime(fornoma)
        firsttxt = open('first.txt',mode='w')
        first = self.firstbin.format(
            self.ver,
            self.url1,
            self.url2,
            self.url3,
            self.eula,
            time
        )
        firsttxt.write(first)
        firsttxt.close()
        os.system('openssl aes-128-cbc -e -in first.txt -out first.bin -K 943B13DD87468BA5D9B7A8B899F91803 -iv 66B33FC1373FE506EC2B59FB6B977C82')
        
def gen():
    #ver = verent.get()
    url1 = url1ent.get()
    url2 = url2ent.get()
    url3 = url3ent.get()
    eula = eulaent.get()
    #print(ver)
    passver = True
    passurl1 = True
    passurl2 = True
    passurl3 = True
    passeula = True
    if url1 == '':
        passurl1 = False
    if url2 == '':
        passurl2 = False
    if url3 == '':
        passurl3 = False
    if eula == '':
        passeula = False
    args = {}
    if passurl1:
        args['url1'] = url1
    if passurl2:
        args['url2'] = url2
    if passurl3:
        args['url3'] = url3
    if passeula:
        args['eula'] = eula
    #print(args['ver'])
    info = FirstBinTemplate(*args)
    info.gen_firstbin()
        
if __name__ == '__main__':
    from tkinter import *
    root = Tk()
    root.title('Wii no Ma Tool')
    wip = Label(root,text='Wii no Ma tool is WIP! Here is a list of WIP functions')
    #wipconfig = Label(root,text='Configuring first.bin (This will be finished very quickly)')
    wiptoday = Label(root,text='Generating today.bin')
    #verl = Label(root,text='Version')
    url1l = Label(root,text='URL 1')
    url2l = Label(root,text='URL 2')
    url3l = Label(root,text='URL 3')
    eulal = Label(root,text='EULA Version')
    #verent = Entry()
    url1ent = Entry()
    url2ent = Entry()
    url3ent = Entry()
    eulaent = Entry()
    gen = Button(root,text='Create first.bin',command=gen)
    wip.pack()
    #wipconfig.pack()
    wiptoday.pack()
    #verl.pack()
    #verent.pack()
    url1l.pack()
    url1ent.pack()
    url2l.pack()
    url2ent.pack()
    url3l.pack()
    url3ent.pack()
    eulal.pack()
    eulaent.pack()
    gen.pack()

