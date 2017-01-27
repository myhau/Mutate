import sys
import commands
import operator

reload(sys)


def get_windows():
    ret = commands.getoutput('wmctrl -l').split('\n')
    names = []
    for line in ret:
        name = line.split(' ')[4:]
        names.append(' '.join(name))
    return names


def match(string, list):
    ret = []
    string = string.lower()
    for item in list:
        lower_item = item.lower()
        m = match_(lower_item,string)
        if m!=-1:
            ret.append((item,m))
    sorted(ret,key=operator.itemgetter(1))
    return [i[0] for i in ret]


def match_(src,target):
    if src is None or len(src)==0 or target is None or len(target)==0:
        return -1
    length = len(src) + len(target)
    c=1.0*(len(src)-len(target)) / len(src)
    d=0
    while len(target)>0:
        position,max_sub_len = get_max_sub(src,target)
        if position == -1:
            return -1
        else:
            src=src[position:]
            target=target[max_sub_len:]
        d+=position
    return 1.0*d/length + c


def get_max_sub(str,target):
    length = len(target)
    while length>0:
        position = str.find(target)
        if position ==-1:
            length-=1
            target=target[:-1]
        else:
            return (position,length)
    return (position,length)

def arg():
    return "".join(sys.argv[1:])


def match_win():
    return match(arg(), get_windows())

if __name__ == '__main__':
    print match2_('abcde','abcde')
    print match2_('abcde', 'a')
    print match2_('abcdefghij-----------------------0daejfiojsoifaeoijoasidfjiaeiofjasdojfaisoejfaasdfjaoeifjasodi ieoajfoiasjefiasjfioa sdfjaeif asijaefjasjaefaiwejfiasdjfoaeojfijasiofj aeofjaiwoejfiasojf asf-------------------------k', 'abk')
