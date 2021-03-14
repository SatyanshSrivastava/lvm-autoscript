#!/usr/bin/env python

import os
import subprocess
import pyfiglet
result = pyfiglet.figlet_format("LVM ", font = "bulbhead"  )
print(result)
def create(pv,vg,lv,size,dire):
        subprocess.call("pvdisplay | grep %s" %(pv), shell=True)
        subprocess.call("vgcreate %s %s" %(vg,pv), shell=True)
        subprocess.call("lvcreate --size {}G --name {} {}".format(size,lv,vg), shell=True)
        subprocess.call(f"mkfs.ext4 /dev/{vg}/{lv}", shell=True)
        subprocess.call(f"mount /dev/{vg}/{lv} {dire}", shell=True)
        os.system(f"lvdisplay /dev/{vg}/{lv}")
        os.system("df -h")
def extend(vg,lv,size_inc):
        os.system(f"lvdisplay /dev/{vg}/{lv}")
        os.system(f"lvextend --size +{size_inc}G /dev/{vg}/{lv}")
        os.system(f"resize2fs /dev/{vg}/{lv}")
        os.system("df -h")
def reduce(vg,lv,size_dec,dire):
        os.system(f"lvdisplay /dev/{vg}/{lv}")
        os.system(f'umount {dire}')
        os.system(f'e2fsck -f /dev/mapper/{vg}-{lv}')
        os.system(f'resize2fs /dev/mapper/{vg}-{lv} {size_dec}G')
        os.system(f'lvreduce -L {size_dec}G /dev/mapper/{vg}-{lv} -y')
        os.system(f'mount /dev/mapper/{vg}-{lv} {dire}')
def remove(lv,vg,dire):
        os.system(f"umount {dire}")
        os.system(f"lvremove /dev/{vg}/{lv} -y")
        os.system("df -h")
while True:
        os.system("tput setaf 3")
        print("Enter 1: For the creation of an LV".upper())
        os.system("tput setaf 3")
        print("Enter 2: For the increment the size of an LV".upper())
        os.system("tput setaf 3")
        print("Enter 3: For the reduction of the size of an LV".upper())
        os.system("tput setaf 3")
        print("Enter 4: For removing a LV".upper())
        os.system("tput setaf 3")
        print("Enter 5: For Exiting".upper())
        os.system("tput setaf 7")
        print("====================================")
        ch=int(input("Enter your choice:".upper()))
        if ch==1:
                pv1=input("Enter the name of the PV you want to create from an existing HDD. eg-/dev/sdb".upper())
                vg1=input("enter the name of the new vg you want to create and thereafter attach PV to the same: ".upper())
                lv1=input("enter the name of the new LV you want to create out of the           existing VG:".upper())
                size1=input("Enter the size of the LV:".upper())
                dire=input("Enter the Directory name".upper())
                if os.path.exists(f"dire"):
                        print(f"Utilizing the directory {dire}".upper())
                else:
                        subprocess.call(f"mkdir {dire}",shell=True)
                create(pv1,vg1,lv1,size1,dire)
                print("====================================")
        elif ch==2:
                pv2=input("Enter the name of the PV. eg-/dev/sdb")
                vg2=input("enter the name of the vg : ".upper())
                lv2=input("enter the name of the LV:".upper())
                size_inc=int(input("Enter the size you want to increase your LV to:".upper()))
                extend(vg2,lv2,size_inc)
                print("====================================")
        elif ch==3:
                vg3=input("enter the name of the vg : ".upper())
                lv3=input("enter the name of the LV :".upper())
                size_dec=int(input("Enter the size you want to reduce your LV to:".upper()))
                dire=input("enter the name of the directory mounted to this LV".upper())
                reduce(vg3,lv3,size_dec,dire)
                print("====================================")
        elif ch==4:
                vg4=input("enter the name of the vg : ".upper())
                lv4=input("enter the name of the LV you want to remove:".upper())
                dire=input("enter the name of the directory mounted to this LV".upper())
                remove(lv4,vg4,dire)
                print("====================================")
        elif ch==5:
                print("Sure, thankyou for coming".upper())
                print("====================================")
                break;
