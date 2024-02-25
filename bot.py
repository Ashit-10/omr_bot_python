# imp may be
import os
#os.system("rm -rf *.session")

## end


from pyrogram import *
import time
import datetime
from random import randint as rain
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
import os
import cv2

tz = pytz.timezone("Asia/kolkata")
sj = BackgroundScheduler(timezone="Asia/kolkata")


git_token = "GITHUB_TOKEN"

import base64
bot_token = 'BOT_TOKEN'
api_id = 'API_ID'
api_hash = 'API_HASH'

tz = pytz.timezone("Asia/kolkata")
import os.path

bot = Client(
    'pyro-boiit',
    bot_token=bot_token,
    api_id=int(api_id),
    api_hash=api_hash
)


from convopyro import Conversation, listen_message

Conversation(bot)


sep = "/"
Owner = 1602293216

ADMINS = [1602293216, 1845525834, 809293242, 19371046]

@bot.on_message(filters.command(["hi"]))
def js(c, m):
   m.reply_text("hello")




from github import Github



@bot.on_message(filters.command("git"))
async def git_(c,m):
    if len(m.text) > 10:
        aa = await m.reply_text("Processing ...")
        fol_told = m.text.split()[1].lower()
        class_name = fol_told.split("_")[0]

        g=Github(git_token)
        repo=g.get_repo("Ashit-10/omr_exams")
        message = "Update files"
        branch = "main"

        try:
            for file in os.listdir(f"{class_name}/{fol_told}/eval_files"):
                file_path = f"{class_name}/{fol_told}/eval_files/{file}"
                image_data = None
                with open(file_path, "rb") as image:
                    f = image.read()
                    image_data = bytearray(f)
                if image_data:
                    repo.create_file(file_path, message, bytes(image_data), branch)
            await aa.edit(f"Successfully uploaded {fol_told}")        
        except Exception as e:
            await aa.edit(str(e))

import os

html_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


"""

@bot.on_message(filters.command(["html", "upload"]))
async def up_html(c, m):
    if len(m.text) > 10:
        aa = await c.send_message(m.chat.id, "Making ...")
        fol_told = m.text.split()[1].lower()
        main_fold = fol_told.split("_")[0]
        global html_str
        html_str += f"""<a href="{fol_told}/result.jpg" download="result"><img src="{fol_told}/result.jpg" alt="jpg" width="380">/</a>     <br><br><br><br>"""
        ranks = []
        for file in os.listdir(f"{main_fold}/{fol_told}/eval_files"):
           ranks.append([int(file.split("_")[0]), file.split(".")[0].split("_")[1]])
       
        ranks1 = sorted(ranks, key=lambda k : [k[0], k])
       # print(ranks1)
        #return
        for fe in ranks1: 
            file = str(fe[0]) + "_" + fe[1] + ".jpg"
            html_str += f"""
    <a href="{fol_told}/eval_files/{file}" download="{file}"><img src="{fol_told}/eval_files/{file}" alt="class 9" width="380"> </a>
        <br>
        <br>
        <br>
        <br> <br>
    """ 

        html_str += "</body>  \n </html>  "
        with open(f"{fol_told}.html", "w+") as wri:
            wri.write(html_str)

        g=Github(git_token)
        repo=g.get_repo("Ashit-10/omr_exams")
        message = "new page"
        branch = "main"
        file_path = f"{fol_told}.html"
        image_data = None
        with open(file_path, "rb") as image:
            f = image.read()
            image_data = bytearray(f)
        if image_data:
            repo.create_file(f"2023/{main_fold}/{file_path}", message, bytes(image_data), branch)
            await aa.edit("Successfully build the page and updated in github.")
            os.remove(file_path)

            await c.send_message(m.chat.id, f"Do you like to upload all files under {fol_told} ?\n[y/n]")
            bb = await listen_message(c, m.chat.id, timeout=10)
            if bb:
                cc = await c.send_message(m.chat.id, f"All files under {fol_told} are being uploaded ...")
                try:
                    file_paths = []
                    for file in os.listdir(f"{main_fold}/{fol_told}/eval_files"):
                        file_paths.append(f"{main_fold}/{fol_told}/eval_files/{file}")
                        file_paths.sort()
                    for file_path in file_paths:
                        image_data = None
                        with open(file_path, "rb") as image:
                            f = image.read()
                            image_data = bytearray(f)
                        if image_data:
                            repo.create_file(f"2023/{file_path}", message, bytes(image_data), branch)

                    file_path = f"{main_fold}/{fol_told}/result.jpg"
                    
                    with open(file_path, "rb") as image:
                            f = image.read()
                            image_data = bytearray(f)
                    if image_data:
                            repo.create_file(f"2023/{file_path}", message, bytes(image_data), branch)

                    await cc.edit(f"Successfully uploaded {fol_told}")        

                except Exception as e:
                    await cc.edit(str(e))

        else:
            await aa.edit("Error while creating page")    
    else:
        await m.reply_text("Did not get the folder name !")







@bot.on_message(filters.command(["up"]))
async def upp(client, message):
    if message.from_user.id == Owner:
         
        try:
            await client.send_document(chat_id=message.chat.id, document=str(message.text.split(' ', 1)[1]))
            await message.reply_text("Done !")
        except Exception as e:
            await message.reply_text(str(e))
            
from omr_utils import *

class_9_students = 35  # Total loop time for asking omr sheets

@bot.on_message(filters.command("set"))
async def set_deefault_folder(c, m):
    if len(m.text) > 8:
        fold = m.text.lower().split()[1]
        with open("default_folder.txt", "w+") as ri:
                ri.write(str(fold))
        await m.reply_text(f"Successfully set the default path to `{fold}`")
    elif m.text.lower().split()[1] == "0":
        os.remove("default_folder.txt")
        await m.reply_text(f"Successfully deleted the default path.")


@bot.on_message(filters.command("eval"))
async def fil_photo(c, m):
#   if len(m.text) < 10:
    chat = m.chat.id
    fol_told=None
    if os.path.exists("default_folder.txt"):
        with open("default_folder.txt", "r") as re:
            fol_told=re.read()
        class_name = f"{fol_told.split('_')[0]}" 
        print("hi")   
    else:
        await c.send_message(chat, "Enter class :") 
        cls_name = None
        cls_name = await listen_message(c, chat, timeout=10)
        if cls_name:
            class_name = f"class-{cls_name.text}"
            folder_name = None
            if not cls_name.text.isdigit():
                await c.send_message(chat, "Error in class name !")
                return
            all_folders = []
            if not os.path.exists(class_name):
                await c.send_message(chat, f"folder {class_name} doesnt exist.")
                return
            avail_folds = []    
            for fold in os.scandir(class_name):
                if fold.is_dir():
                    folder_name=fold.path.split("/")[1]
                    all_folders.append(folder_name)
                 
            #        print(folder_name)
            fol_name_str = ""
            for fo in all_folders:
                fol_name_str += f"**{all_folders.index(fo) + 1}**. `{fo}`" + "\n"
                avail_folds.append(fo)
            await c.send_message(chat, f"select folder name:\n{fol_name_str}")
            fol_tell = None
            fol_tell = await listen_message(c, chat, timeout=10)

            if fol_tell:
                if fol_tell.text.isdigit():
                    fol_told = avail_folds[int(fol_tell.text) - 1]
                else:
                    fol_told = fol_tell.text.lower()
                print(fol_told)
                if fol_told in all_folders:
                    await c.send_message(chat, f"Selected folder = `{fol_told}`")
                else:
                    await c.send_message(chat, f"Folder {fol_told} not found ! ")
                    return
            # return
        else:
            await c.send_message(chat,"Timeout")
        
    if fol_told:
        main_fold = f"{class_name}/{fol_told}"
        await c.send_message(chat, f"{class_name}/{fol_told} is ready to being evaluated.\nYou can send photos as per roll number.")
        
        for n in range(0, class_9_students):
            get_filee=None
            cap_given = None
            get_filee = await listen_message(c, chat, timeout=40)
            if get_filee:
                if get_filee.photo:   
                    if get_filee.caption:
                        file_name = get_filee.caption
                        cap_given = True
                    else:
                        file_name = n + 1            
                    aa = await c.send_message(chat, f"Downloading {file_name}.jpg...")
                    go_on = True
                    if os.path.exists(f"{main_fold}/og_files/{file_name}.jpg"):
                        get_con = None
                        go_on = None
                        jpg_ = await c.send_message(chat, f"{main_fold}/og_files/{file_name}.jpg already exists,\nReplace it ? \n[y/n]")
                        get_con = await listen_message(c, chat, timeout=0.1)   # not working
                        if get_con:
                            if get_con.text.lower() != "y":
                                await c.send_message(chat, "Operation abroated !")
                                break
                            else:
                                # await jpg_.delete()
                                go_on = True
                        else:
                     #       await c.send_message(chat, "No responce got, proceeding with replacing the oler file.")
                            go_on = True
                        await jpg_.delete()
                    if go_on:
                        try:
                            os.system(f"rm -f {main_fold}/og_files/{file_name}.jpg")
                            os.system(f"rm -f {main_fold}/eval_files/{file_name}_*")

                        except Exception as e:
                            print(e)
                        await get_filee.download(f"{main_fold}/og_files/{file_name}.jpg")
                        await aa.edit(f"Scanning ... {file_name}")

                        eval_file = await read_img(f"{main_fold}/og_files/{file_name}.jpg",
                                                    f"{main_fold}/eval_files/{file_name}", f"{main_fold}/{fol_told}_ans_key.txt", f"{main_fold}/eval_files", file_name, cap_given)
                        
                        if not eval_file:
                            await c.send_message(chat, "Photo was not clear enough , Please re-do.")
                            await aa.delete()
                            break

                        selected = eval_file[1]
                        correct = eval_file[2]
                        wrong = eval_file[3]
                        total_keys = eval_file[4]
                        actual_roll = eval_file[6]
                        file_name = eval_file[5]
                        hash_class = class_name.split("-")[1]
                        bb = await aa.edit("successfully Evaluated .\nUploading ...")
                        if int(selected) == 0:
                            await bb.edit("Student didnt answer anything, so it will count as absent .")
                            return
                        if os.path.exists(f"{class_name}{sep}{class_name}_rolls.txt"):
                            with open(f"{class_name}{sep}{class_name}_rolls.txt", "r") as ro:
                                roll_names = json.load(ro)
                                if actual_roll.startswith("0"):
                                    actual_roll = actual_roll[1:]
                                    print(actual_roll, "replaced roll 0")
                                kid_name = roll_names.get(actual_roll)
                                
                        await get_filee.reply_photo(f"{file_name}_{correct}.jpg", caption = f""" 
Class: class-{hash_class}    
Exam: #{fol_told.replace("-", "_")}
Name: __{kid_name}__
Roll no: {actual_roll}  
Total_mark: {total_keys}                                          
correct: **{correct}**
Wrong: {wrong}
Not selected: {selected}

    """)
                        await aa.delete()

                elif get_filee.text and "end" in get_filee.text .lower():
                    await c.send_message(chat, "Evaluation ended.")   
                    break
            else:
                await c.send_message(chat,"Timeout Error has been occured. Please re-do command .")
                break

    await c.send_message(chat,"Timeout;")

import os


@bot.on_message(filters.command("result"))
async def show_result(c, m):
    chat = m.chat.id
    await c.send_message(chat, "Enter class :") 
    
    cls_name = None
    mark_list = {}
    fans={}
    cls_name = await listen_message(c, chat, timeout=10)
    if cls_name:
        class_name = f"class-{cls_name.text}"
        folder_name = None
        if not cls_name.text.isdigit():
            await c.send_message(chat, "Error in class name !")
            return
        all_folders = []
        for fold in os.scandir(class_name):
            if fold.is_dir():
                folder_name=fold.path.split(sep)[1]
                all_folders.append(folder_name)
              #  print(folder_name)
        fol_name_str = ""
        avail_folds = []
        for fo in all_folders:
            fol_name_str += f"**{all_folders.index(fo) + 1}**. `{fo}`" + "\n"
            avail_folds.append(fo)
        await c.send_message(chat, f"select folder name:\n{fol_name_str}")
        fol_tell = None
        fol_tell = await listen_message(c, chat, timeout=10)
        if fol_tell:
            if fol_tell.text.isdigit():
                fol_told = avail_folds[int(fol_tell.text) - 1]
            else:
                fol_told = fol_tell.text.lower()
            print(fol_told)
            if fol_told in all_folders:
                await c.send_message(chat, f"Selected folder: {fol_told}")
            else:
                await c.send_message(chat, f"Folder {fol_told} not found ! ")
                return
            main_fold = f"{class_name}/{fol_told}"
            res = {}
            rank_list = []
            ev = await c.send_message(chat, "Evaluating ...")

            for fold in os.listdir(f"{main_fold}{sep}eval_files"):
                if os.path.isfile(f"{main_fold}{sep}eval_files{sep}{fold}"):
                    file = fold
                    # print(file)
                    roll = file.split("_")[0]
                    mark = file.split("_")[1].split(".")[0]
                    res.update({roll : mark})
                    rank_list.append([roll, mark])
            rank_roll = {}
            seriel_rank = sorted(rank_list, key=lambda k : [int(k[0]), k])
           # print(seriel_rank)
            rank_list_sort = sorted(rank_list, key=lambda k : [int(k[1]), k])
            rank_list_sort.reverse()
           # print(rank_list_sort)
            rank_str = f"**{class_name}**\n{fol_told}\n--Roll--    --mark--\n"
            
            roll_N = None
            rannk = 1
            for ra in rank_list_sort:
                hi = ra[1]  #mark
                rank_str += f" {ra[0]}   -   {hi}\n"
                if roll_N:
                    if (hi != roll_N):
                        rannk += 1
                rank_roll.update({ra[0] : rannk})
                roll_N = hi


            await ev.edit(rank_str)
            for i in seriel_rank:
                fans.update({i[0] : i[1]}) 

            with open(f"{main_fold}/{fol_told}_result.txt", "w+") as r:
                json.dump(fans, r, indent=6)  
            await c.send_document(chat, f"{main_fold}{sep}{fol_told}_result.txt")    
            
            # print(rank_str)
            img = cv2.imread("sheet.jpg")
            with open(f"{main_fold}{sep}{fol_told}_ans_key.txt", "r") as red:
                total_que_file = json.load(red)
            # print(len(total_que_file))
            total_que = str(len(total_que_file))
            x1 = 50
            y1 = 190
            fol_told = (fol_told[fol_told.find("_") + 1 :]).replace("_", " - ")
            c_date = datetime.datetime.now()
            exam_date = c_date.strftime("%d-%m-%Y")
            cv2.putText(img, cls_name.text, (180, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
            cv2.putText(img, fol_told, (430, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2, cv2.LINE_AA)
            cv2.putText(img, f"Date: {exam_date}", (430, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2, cv2.LINE_AA)
            
            if os.path.exists(f"{class_name}{sep}{class_name}_rolls.txt"):
                with open(f"{class_name}{sep}{class_name}_rolls.txt", "r") as ro:
                    roll_names = json.load(ro)
            print(seriel_rank)
            y2 = None
            for aa in roll_names: #seriel_rank:
                a = None
                for i in seriel_rank:
                    if str(i[0]) == aa:
                        a = i
     
                try:
                        total_marks = str(total_que)
                        got_mark = str(a[1])
                        his_rank = str(rank_roll.get(a[0]))
                except:
                         total_marks = "--"
                         got_mark = "--"
                         his_rank = "--"
                if his_rank == "1":
                     his_rank = "1" # + str(emo.emojize(':1st_place_medal:'))
                elif his_rank == "2":
                    his_rank = "2" # + str(emo.emojize(':2nd_place_medal:'))
                elif his_rank == "3":
                    his_rank = "3" #3+ str(emo.emojize(':3rd_place_medal:'))


                # string = f"{a[0]} {roll_names[a[0]]}         {total_que}                 {a[1]}            {rank_roll.get(a[0])}"
                cv2.putText(img, f"{aa}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2, cv2.LINE_AA)
                cv2.putText(img, f"{roll_names[aa]} ", (x1 + 80, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2, cv2.LINE_AA)
                cv2.putText(img, total_marks, (x1 + 350, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2, cv2.LINE_AA)
                cv2.putText(img, got_mark, (x1 + 450, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2, cv2.LINE_AA)
                cv2.putText(img, his_rank, (x1 + 560, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0), 2, cv2.LINE_AA)



                y1 += 35
                y2 = y1
            # cv2.imshow("ll", img)    
            print(y2)
            shape = img.shape
            crop = img[0:y2 + 50, 0:980]
            # cv2.imshow("kki", crop)
            # cv2.waitKey(0)
            cv2.imwrite(f"{main_fold}{sep}result.png", crop)
            await c.send_photo(chat, f"{main_fold}{sep}result.png")
            # cv2.imshow("kki", img)
            # cv2.waitKey(0)
import re

@bot.on_message(filters.command("update"))
async def update_ans_key(c, m):
    if m.reply_to_message:
        texts = m.reply_to_message.text.lower()
        try:
            class_name_ = texts.split("\n")[0] 
            class_name_got = class_name_.split("_")[0]
            astr =texts.split("\n")[1]
        except:
            await m.reply_text("Write class and exam name on the first line.\neg: `class-10_english_2`")
            return
        
        astr = astr.replace(" ", "").replace(" ", "").replace(" ", "").replace(",", "")
        ans_key = {}
        bstr = re.findall(r"\d+", astr)
        for aa in bstr:
            astr = astr.replace(aa, "", 1)

        dstr = astr.split("-")
        dstr.pop(0)
        for cc in bstr:
            opts = dstr[bstr.index(str(cc))]
            multi_opts = []
            for multi in opts:
                multi_opts.append(multi.upper())

            ans_key.update({cc: multi_opts})

        with open(f"{class_name_got}{sep}{class_name_}{sep}{class_name_}_ans_key.txt", "w+") as wr:
                        json.dump(ans_key, wr, indent=6)

        await c.send_message(m.chat.id, f"Successfully updated the file {class_name_got}{sep}{class_name_}{sep}{class_name_}_ans_key.txt")
        await c.send_document(m.chat.id, f"{class_name_got}{sep}{class_name_}{sep}{class_name_}_ans_key.txt")


@bot.on_message(filters.command("start"))
async def start(c, m):
    chat_id = m.chat.id
    aa = await c.send_message(chat_id, "Enter class name: ")
    class_name = None
    subject = None
    ans_key_file = None

    class_name = await listen_message(c, m.chat.id, timeout=10)
    class_name_got = f"class-{class_name.text}"
    if class_name:
        print(class_name.text)
        await c.send_message(chat_id, f"Class = {class_name_got}\nEnter subject :")
        subject = await listen_message(c,m.chat.id, timeout=10)
        if subject:
            subject_name = subject.text.lower()
            for f in range(1, 100):
                folder_name = f"{class_name_got}_{subject_name}_{f}"
                if not os.path.exists(f"{class_name_got}"):
                    os.mkdir(class_name_got)
                if not os.path.exists(f"{class_name_got}/{folder_name}"):
                    make_fold = os.mkdir(f"{class_name_got}/{folder_name}")
                    os.mkdir(f"{class_name_got}/{folder_name}/og_files")
                    os.mkdir(f"{class_name_got}/{folder_name}/eval_files")

                    break
            await subject.reply_text(f"""Folder **{class_name_got}/{folder_name}** has been created and ready to use .
                                     \nYou can Now send the Answer key ..\n(Within 20 seconds)""")
            ans_key_file = await listen_message(c, chat_id, timeout=20)
            ans_key_file_name = f"{folder_name}_ans_key.txt"
            if ans_key_file:
                    try:
                    	astr = ans_key_file.text.split("\n")[1]
                    except Exception as e:
                        print(e)
                        astr = ans_key_file.text
                 

                    astr = astr.replace(" ", "").replace(" ", "").replace(" ", "").replace(",", "")
                    ans_key = {}
                    bstr = re.findall(r"\d+", astr)
                    for aa in bstr:
                        astr = astr.replace(aa, "", 1)

                    dstr = astr.split("-")
                    dstr.pop(0)
                    for cc in bstr:
                        opts = dstr[bstr.index(str(cc))]
                        multi_opts = []
                        for multi in opts:
                            multi_opts.append(multi.upper())
                        ans_key.update({cc: multi_opts})

                    with open(f"{class_name_got}/{folder_name}/{ans_key_file_name}", "w+") as wr:
                        json.dump(ans_key, wr, indent=6)
                    print(ans_key)
                    await c.send_message(chat_id, f"Answer key has been successfully saved, you should check the file below once.")
                    await c.send_document(chat_id, f"{class_name_got}/{folder_name}/{ans_key_file_name}")

                    # with open("locations.txt") as ed:
                    #     locs = json.load(ed)
                 
                    # image = cv2.imread("blank_sheet.jpg")
                    # for ser_num in ans_key:
                    #     x = int(ser_num)
                    #     [pre_y] = ans_key[ser_num]
                   
                    #     y = None
                    #     if pre_y == "A":
                    #        y = 1
                    #     elif pre_y == "B":
                    #        y = 2
                    #     elif pre_y == "C":
                    #        y = 3
                    #     elif pre_y == "D":
                    #        y = 4
                    #     else:
                    #         print("didnt get the y")
                    #         y = None
                    #     if y:
                    #         opt_num = 4 * (x - 1) + y
                    #         [a, b] = locs.get(str(opt_num))
                     
                    #         cv2.circle(image, (a, b), 2, (238, 48, 167), 7)  # pink
                    # cv2.imwrite("ans.jpg", image)
                    # await c.send_document(chat_id, "ans.jpg")
                    # os.remove("ans.jpg")
                    eval_file = await read_img(f"blank_sheet.jpg",
                                                    f"ans", f"{class_name_got}/{folder_name}/{ans_key_file_name}", None, None, True)
                    await c.send_photo(chat_id, "ans_0.jpg")
                    
                        

            else:
                await c.send_message(chat_id, "timeout")
                 

        else:
            await c.send_message(chat_id, "timeout")

    else:
        await c.send_message(chat_id, "timeout")
import shutil
    
@bot.on_message(filters.command("del"))
async def dele(c, m):
     yes_or_no = None
     fname = m.text.lower()
     class_name = fname.split()[1].split("_")[0]
    #  print(class_name)
    #  print(fname)
     main_file = f"{class_name}/{fname.split()[1].lower()}"
     await m.reply_text(f"Delete {main_file} ?\nAre you sure ?\n[y/n]")
     yes_or_no = await listen_message(c, m.chat.id, timeout=10)
     if yes_or_no and yes_or_no.text.lower() == "y":
          try:
            shutil.rmtree(main_file) 
            await c.send_message(m.chat.id, f"Successfully deleted {main_file}")
          except Exception as e:
               await c.send_message(m.chat.id, str(e))

     else:
          await c.send_message(m.chat.id, "TImeout")


def exc(client, m):
    if m.text.startswith('$'):
        cmd = m.text[1:]
        tes = m.reply_text('`Processing ...`')
        idk = str(rain(0000000000, 9999999999))

        output=os.system(f"{cmd} > null/{idk}.txt")
        if output or str(output) == "0":
           with open(f"null/{idk}.txt", 'r') as se:
             output = se.read()
        try:
            tes.edit(str(output))
        except Exception as e:
            if str(e) == """Telegram says: [400 MESSAGE_TOO_LONG] - The message text is over 4096 characters (caused by "messages.EditMessage")""":
               tes.delete()
               m.reply_document(f"null/{idk}.txt")
            elif str(e) == """Telegram says: [400 MESSAGE_EMPTY] - The message sent is empty or contains invalid characters (caused by "messages.EditMessage")""":
               tes.edit("Empty output !")
            else:
                tes.edit(str(e))
        finally:
           os.system(f"rm -rf null/{idk}.txt")


@bot.on_message(filters.user(Owner) & filters.regex("$"))
def okey(c, m):
    if m.text and m.text.startswith("$"):
        exc(c, m)
   


bot.run()
