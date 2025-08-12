import TkEasyGUI as eg

def build_checkbox(member_list):
    sorted_members = [
        ["花海咲季","Saki"],
        ["月村手毬","Temari"],
        ["藤田ことね","Kotone"],
        ["有村麻央","Mao"],
        ["葛城リーリヤ","Lilja"],
        ["倉本千奈","China"],
        ["紫雲清夏","Sumika"],
        ["篠澤広","Hiro"],
        ["姫崎莉波","Rinami"],
        ["花海佑芽","Ume"],
        ["秦谷美鈴","Misuzu"],
        ["十王星南","Sena"],
        ["A","A"],
        ["B","B"],
        ["C","C"],
        ["D","D"]
    ]
    checkbox = ""
    for member in sorted_members:
        if member in member_list:
            if checkbox != "":
                checkbox +="\n"
            checkbox +=   f"    <label><input type=\"checkbox\" class=\"part-toggle\" value=\"{member[1]}\">{member[0]}</label>" 
    return checkbox


def format_html(title="ここにタイトルが入る",members="ここにメンバーのチェックボックスが入る",lyrics="ここに歌詞が入る",):
    str = \
    f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="学園アイドルマスター収録『{title}』のキャラクター別歌詞表示ページです">
    <meta name="keyword" content="学マス　学園アイドルマスター　{title.replace(" ","_")}　歌詞　キャラ別　パート分け　最強リセマラランキング">
    <meta name="author" content="篠沢広は声を張れbot">
    <meta name="robots" content="index, follow">
    <title>White Night! White Wish!</title>
</head>
<body>
    <header>
        <h1>{title}</h1>
    </header>
    <div id = "creater-info">作詞・作曲・編曲：</div>
    <埋め込みリンク>
    <link rel=\"stylesheet\" href=\"style.css\">
    <hr>
{members}

    <div id=\"lyrics\">
{lyrics}
    </div>

    <div id="sidebar"></div>
    <footer>
        <hr>
        <span class="copy_right">
          当サイトに掲載されているすべてのコンテンツの著作権は、各権利者に帰属します。
        </span>
    </footer>

    <script src=\"script.js\"></script>
    <script>
        fetch("sidebar.html")
            .then(response => response.text())
            .then(html => {{
            document.getElementById("sidebar").innerHTML = html;
            }});
    </script>

</body>
</html>
"""

    return str

def convert_lyrics(lyric,member,previous):
    txt = previous + f"             <span class=\"line\" data-part=\"{" ".join(member)}\">" + \
        lyric +\
        "</span>\n"

    return txt

def build_layout(title):
    layout = [
        [eg.Text("歌詞のhtmlつくるメーカー",font=("normal",20,"bold"))],
        [
            eg.Checkbox("花海咲季",key="-partinfo Saki",metadata={"part":"Saki"}),
            eg.Checkbox("月村手毬",key="-partinfo Temari",metadata={"part":"Temari"}),
            eg.Checkbox("藤田ことね",key="-partinfo Kotone",metadata={"part":"Kotone"}),
            eg.Checkbox("有村麻央",key="-partinfo Mao",metadata={"part":"Mao"})
        ],
        [
            eg.Checkbox("葛城リーリヤ",key="-partinfo Lilja",metadata={"part":"Lilja"}),
            eg.Checkbox("倉本千奈",key="-partinfo China",metadata={"part":"China"}),
            eg.Checkbox("紫雲清夏",key="-partinfo Sumika",metadata={"part":"Sumika"}),
            eg.Checkbox("篠澤広",key="-partinfo Hiro",metadata={"part":"Hiro"})
        ],
        [
            eg.Checkbox("姫崎莉波",key="-partinfo Rinami",metadata={"part":"Rinami"}),
            eg.Checkbox("花海佑芽",key="-partinfo Ume",metadata={"part":"Ume"}),
            eg.Checkbox("秦谷美鈴",key="-partinfo Misuzu",metadata={"part":"Misuzu"}),
            eg.Checkbox("十王星南",key="-partinfo Sena",metadata={"part":"Sena"})
        ],
        [
            eg.Checkbox("A",key="-partinfo A",metadata={"part":"A"}),
            eg.Checkbox("B",key="-partinfo B",metadata={"part":"B"}),
            eg.Checkbox("C",key="-partinfo C",metadata={"part":"C"}),
            eg.Checkbox("D",key="-partinfo D",metadata={"part":"D"})
        ],
        [
            eg.InputText(key="lyrics",size=[100,40])
        ],
        [
            eg.Button("↓",key="-event convert"),
            eg.Button("改行",key="-event br"),
            eg.Button("空白挿入",key="-event blank"),
            eg.Button("空白挿入(半角)",key="-event halfblank"),
            eg.Button("Undo",key="-event undo")
        ],
        [
            eg.Column(layout=[
                [eg.Multiline(format_html(title=title),key="converted_lyrics",expand_x=True,expand_y=True)]
            ],width=200,size=[200,500], expand_y=True,expand_x=True)
        ],
        [eg.HSeparator()],
        [
            eg.Column(layout=[
                [
                    eg.Button("Export HTML",key="-event export"),
     
                ]
            ],text_align="right",expand_x=True)
        ]
    ]

    return layout

def main():

    title = eg.popup_input("曲名をいれろよぃ")

    layout = build_layout(title)
    window = eg.Window("歌詞パートわけするぴょん",layout,resizable = True)
    member_list = []
    converted_lyrics=""
    member_checkbox = ""
    undood = True
    

    while True:    
        event, values = window.read()
        if event == "-event convert":
            Checked_keylist = [k for k,v in values.items() if k.startswith("-partinfo") and v]
            Checked_memberlist = []
            for k in Checked_keylist:
                Checked_memberlist.append(
                    window[k].metadata["part"]
                )
                if not [window[k].props["text"],window[k].metadata["part"]] in member_list:
                    member_list.append([window[k].props["text"],window[k].metadata["part"]])
            
            prev_lyrics = converted_lyrics
            converted_lyrics = convert_lyrics(values["lyrics"],Checked_memberlist,prev_lyrics)
            prev_member_checkbox = member_checkbox
            member_checkbox = build_checkbox(member_list)
            window["converted_lyrics"].update(text=format_html(title=title,members=member_checkbox,lyrics=converted_lyrics))
            prev_input = values["lyrics"]
            window["lyrics"].update(text="")
            undood = False

        if event =="-event br":
            converted_lyrics = converted_lyrics + "             <br>\n"
            window["converted_lyrics"].update(text=format_html(title=title,members=member_checkbox,lyrics=converted_lyrics))

        if event =="-event blank":
            converted_lyrics = converted_lyrics + "{blank}"
            window["converted_lyrics"].update(text=format_html(title=title,members=member_checkbox,lyrics=converted_lyrics))

        if event =="-event halfblank":
            converted_lyrics = converted_lyrics + "{half_blank}"
            window["converted_lyrics"].update(text=format_html(title=title,members=member_checkbox,lyrics=converted_lyrics))

        if event == "-event undo":
            if undood:
                eg.popup("やり直しは一回きりだぜベイベ")
            else:
                converted_lyrics = prev_lyrics
                window["converted_lyrics"].update(text=format_html(title=title,members=prev_member_checkbox,lyrics=prev_lyrics))
                window["lyrics"].update(text=prev_input)
                undood = True
        
        if event == "-event export":
            filename = eg.popup_input("保存するファイル名を入力してください（.htmlは自動で付きます）")
            formated_lyrics = values["converted_lyrics"].replace(">\n{blank}",">　\n").replace(">\n{half_blank}","> \n")
            if filename:
                if not filename.endswith(".html"):
                    filename += ".html"
                try:
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(formated_lyrics)
                    eg.popup("保存しました！", filename)
                except Exception as e:
                    eg.popup_error("保存に失敗しました…", str(e))



        if event in eg.WINDOW_CLOSED:
            break

if __name__ == "__main__":
    main()
