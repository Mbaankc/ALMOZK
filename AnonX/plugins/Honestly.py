import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client

#▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▒▒▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▇▇▒▒▒▒▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▇▇▇▇▒▒▇▇▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▇▇▇▇▇▒▒▇▇▇▇▇▇▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▇▇▒▇▇▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▇▒▒▇▇▇▇▇▇▇▇▇▇▒▒▇▇▒▒▒▒▇▇▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▇▇▇▇▒▒▒▒▒▒▒▒▇▇▇▇▇▒▒▆▆▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▜▒▒▇▇▒▒▆▆▆▆▆▆▆▆▆
#▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▇▇▇▒▒▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▇▇▇▒▒▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▇▇▒▒▇▇▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▇▇▇▒▒▒▒▒▇▇▒▒▒▒▒▇▇▒▒▒▇▇▒▒▒▒▒▒▒▒▇▇▇▒▒▒▒▇▇▒▒▆▆▒▒▒▒▒▒▒
#▒▇▇▒▒▒▒▒▒▒▒▒▒▒▒▒▇▇▒▒▒▒▒▒▇▇▇▇▇▒▒▒▒▙▇▇▇▇▇▇▉▒▒▒▒▇▇▒▒▇▇▇▇▇▇▇▇▇
#▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒𝐊𝐈𝐌𝐌𝐘 𝐊𝐈𝐍𝐆 𝐕𝐄𝐆𝐀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒


txt = [

            "هل تخربني اسم والدتك ما هو.",


            "ليك اسم شهره بتحبو ؟",
            

            "ممكن تعمل اي في حياتك",
            
            
            "انت راضي عن حياتك",
            
            
            "اسم حببتك الاوله ايه",
            
            
            "ما هو هدفك في الحياه",
            
            
            "كم مجموعك الدراسي",
            
            
            "ما هو الاكل المفضل لك",
            
            
            "هل تحب سماع القران الكريم",
            
            
            "هل تامن بالحب",
            
            
            "ماهو اخطر سر اليك",
            
            
            "هل تامن بالارتباط السوشيال",
            
            
            "متي ستتزوج",
            
            
            "هل تحب الفتيات ام الصبيان",
            
            
            "ماهو قولك عندما تره ما تحب",
            
            
            "مانوع هاتفك الجوال",
            
            
            "ماذا تفعل في الشتاء",
            
            
            "هل تحب والديك ام خوتك",
            
            
            "هل لك اسم شهره",
            
            
            "سبق و فعلت شي ندمان علي فعله",
            
            
            "ما هو هدفك في الوقت الحالي",
            
            
            "ما اسم فلمك المفضل",
            
            
            "هل تحب الصراحه ام الكذب",
            
            
            "• أوصف نفسك بكلمة؟",
            
            
            "ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",
            
            "تاريخ ميلادك ايه?",
            
            
            "مرتبط ولا سنجل ؟",
            
            
            "انت بخير حاليا ؟",
            
            
            "اسمك ايه",
            
            
            "منين داهيه",
            
            
            "عندك صحاب بنات",
            
            
            "عندك صحاب ولاد",
            
            
            "لونك المفضل",
            
            
            "جربت حاجه نجحت واي هي ؟",
            
            
            "رايك في البار",
            
            
            "مين اكتر حد بتحبه هنا",
            
            
            "هات رقمك",
            
            
            "بتحب المغامره",
            
            
            "احسن حاجه حصلتلك الفتره دي",
            
            
            "بتصلي",
            
            
            "كم فرد في الاسلام",
            
            
            "ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",
            
            
            "كم ركعه في صلاه العصر",
            
            
            "ما هيا اليلله التي خير من الف شهر",
            
            
            "سرقت قبل كدا",
            
            
            "هل تحب الموسيقى",
            
            
            "هل تحب مصر",
            
            
            "لو الحمه غلت تاكل ايه",
            
            
            "ايه رايك فيا كابوت موز",
            
            
            "بتحب مين من الفنانين",
            
            
            "امك حلوه",
            
            
            "عندك كم اخ",
            
            
            "تقدر تنصح غيرك",
            
            
            "عاوز تعمل نصيبه امتي",
            
            
            "اي اللي مخليك فجروب الزباله دا",
            
            
            "لابس ايه دلوقتي",
            
            
            "لابسه ايه دلوقتي",
            
            
            "حد باسك قبل كدا",
            
            
            "بوست حد قبل كدا",
            
            
            "بتحب الفلوس",
            
            
            "بتحب الكشري",
            
            
            "نفسك تسافر فيه",
            
            
            "عالطلاق انت كحيااان",
            
            
            "بتعرف ترقص",
            
            
            "بتعرف تغني",
            
            
            "بتحب المدرسه",
            
            
            "ارتبط من المدرسه قبل كدا",
            
            
            "اكتر اتنين بتحب تخرج معاهم",
            
            
            "بتحب الفصح",
            
            
            "بتحب المناسبات",
            
            
            "بتحب الفول",
            
            
            "عاوز تخرج فين",
            
            
            "جربت تموت من الجوع قبل كدا",
            
            
            "بتحب تربي القطط",
            
            
            "مامتك عايشه",
            
            
            "ايه رايك في تليجرام",
            
            
            "ايه رايك في بت اللي فكول دي",
            
            
            "ايه رايك في اسعار في البلد",
            
            
            "ناوي تغير فونك امتي",
            
            
            "تعرف تشتم حد بتحبو",
            
            
            "بتحب الصعيد",
            
            
            "بتحب اسكندريه",
            
            
            "متابع ايه في مسلسلات التركي",
            
            
            "عندك واتساب",
            
            
            "ايه رايك في الشتاء",
            
            
            "ايه رايك في الصيف",
            
            
            "ايه رايك في الخريف",
            
            
            "كم فصل في سنه",
            
            
            "قاعد فين دلوقتي",
            
            
            "شربت حشيش قبل كدا",
            
            
            "بتشرب سجاير",
            
            
            "بتشربي سجاير",
            
            
            "عيط علي حاجه قبل كدا",
            
            
            "بتنام امتي",
            
            
            "شغال ايه",
            
            
            "شغاله ايه",
            
            
            "بتحب شغالك",
            
            
            "نفسك تبقي غني",
            
            
            "بتعرف تخبي مشعارك",
            
            
            "لون عيونك ايه",
            
            
            "لون شعرك ايه",
             "حبيت كام مره 💏",
             
                "اتعاكست كام مره☹️☹️",
                
                "خونت كام مره 😈",
                
                "موقف محرج حصلك😳",
                
                "اكتر شخص حبيته وكسرك💔",
                
                "شايف نفسك فين  بعد 5 سنين🤑",
                
                "لو بقيت بنت ليوم اول حاجه هتعملها ايه والعكس لو بقيتي ولد ليوم اول حاجه هتعمليها ايه🤐🤐",
                
                "اغرب موقف حصلك🤨",
                
                "اقرب انسان لقلبك 💑",
                
                "قولي اغلي 5 اشخاص في حياتك 👨‍👩‍👦‍👦",
                
                "اوصف نفسك في كلمتين👼",
                
                "لو ليك 3 امنيات هيبقوا ايه 🧚‍♂️🧚‍♀️",
                
                "اكتر شخص بتحبه هنا مين😍",
                
                "اوصف صاحب ليك في 3 كلمات😌",
                
                "عاكست قبل كده وكان مين😘",
                
                "اتخانت قبل كده ؟🤣",
                
                "لو اتجبرت علي جواز صالونات هتوافق 👰🤵",
                
                "لو هترتبط بحد في الروم هيبقي مين 😉",
                
                "اهلك بيدلعوك بيقولولك ايه 😁😁",
                
                "صوتك حلو؟",
                
                "لقيت الناس اللي بوشين؟",
                
                "شيء وكنت تحقق اللسان؟",
                
                "أنا شخص ضعيف عندما؟",
                
                "هل ترغب في إظهار حبك ومرفق لشخص أو رؤية هذا الضعف؟",
                "هل الكذب يكون ضروري وقتا ما؟",
                
                "أتشعر بالوحدة على الرغم انه يحاط بك الكثير من البشر؟",
                
                "كيفية الكشف عن من يكمن عليك؟",
                
                "إذا حاول شخص ما أن يكرهه أن يقترب منك ويهتم بك تعطيه فرصة؟",
                
                "أشجع حاجه حلوه ف حياتك؟",
                
                "طريقة جيدة يقنع حتى لو كانت الفكرة خاطئة" 
                
                "كيف تتصرف مع من يسيئون فهمك ويأخذ على ذهنه ثم ينتظر أن يرفض؟",
                
                "التغيير العادي عندما يكون الشخص الذي يحبه؟",
                
                "المواقف الصعبة تضعف لك ولا ترفع؟",
                
                "نظرة و يفسد الصداقة؟",
                
                "‏‏لو حد قالك كلام سئ في الغالب اي رد فعلك؟",
                
                "شخص معاك بالحلوه والمُره؟",
                
                "‏هل تحب إظهار حبك وتعلقك بالشخص أم ترى ذلك ضعف؟",
                
                "تاخد بكلام اللي ينصحك وماتعملش اللي انت عاوزة؟",
                
                "اي تتمني الناس تعرفه عليك؟",
                
                "ابيع المجرة عشان؟",
                
                "أحيانا بحس ان الناس ، كمل؟",
                
                "صدفة العمر الحلوة هي اني؟",
                
                "الكُره العظيم دايم يجي بعد حُب قوي "
                "صفة تحبها في نفسك؟",
                
                "‏الفقر فقر العقول ليس الجيوب "
                
                "تصلي صلواتك الخمس كلها؟",
                
                "‏تجامل أحد على راحتك؟",
                
                "اشجع شيء عملته ف حياتك؟",
                
                "ناوي تعمل اي النهارده؟",
                
                "اي بيكون شعورك لما بتشوف المطر؟",
                "غيرتك هاديه ومابتعملش مشاكل؟",
                "اي اكتر حاجه ندمت عليها؟",
                "اي الدول اللي تتمنى تزورها؟",
                "اخره مره بكيت امتي؟",
                "تقييم حظك ؟ من عشره؟",
                "هل تعتقد ان حظك سيئ؟",
                "شـخــص تتمنــي الإنتقــام منـــه؟",
                "كلمة تود سماعها كل يوم؟",
                "**هل تُتقن عملك أم تشعر بالممل؟",
                "هل قمت بانتحال أحد الشخصيات لتكذب على من حولك؟",
                "متى آخر مرة قمت بعمل مُشكلة كبيرة وتسببت في خسائر؟",
                "ما هو اسوأ خبر سمعته بحياتك؟",
                
                "‏ هل جرحت شخص تحبه من قبل ؟",
                
                "ما هي العادة التي تُحب أن تبتعد عنها؟",
                "‏هل تحب عائلتك ام تكرههم؟",
                "‏من هو الشخص الذي يأتي في قلبك بعد الله – سبحانه وتعالى- ورسوله الكريم – صلى الله عليه وسلم؟",
                "‏هل خجلت من نفسك من قبل؟",
                
                "‏ما هو ا الحلم الذي لم تستطيع ان تحققه؟",
                
                "‏ما هو الشخص الذي تحلم به كل ليلة؟",
                
                "‏هل تعرضت إلى موقف مُحرج جعلك تكره صاحبهُ؟",
                "‏هل قمت بالبكاء أمام من تُحب؟",
                
                "‏ماذا تختار حبيبك أم صديقك؟",
                
                "‏ اي رأيك في سورس مانجا",
                
                "ما هي أجمل سنة عشتها بحياتك؟",
                
                "‏ما هو عمرك الحقيقي؟",
                
                "ما هي أمنياتك المُستقبلية؟"
          
            
            
            

        ]


        


@app.on_message(command(["اصراحه","اسال","س","سوال","اس"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
