from tkinter import *
from tkinter.font import *
from tkinter.messagebox import *
import pickle
import tkinter.ttk as ttk
from main_algorithm import *
import pandas as pd

#df = pd.read_csv('data/for_model_final_pre.csv', encoding = "utf-8-sig")
#df = df.sample(frac=1, random_state=2020).reset_index(drop=True)
#train = df[:401000] # 70%
#val = df[401000:486928]
#test = df[486928:]
#str_features = ["user", "item_name", "item_brand", "item_category1", "item_category2", "item_category3"]
#int_features = ["review", "item_sale_price", "item_score", "item_count", "n1", "n2", "n3", "n4", "c6", "total_score", "dur_score", "price_score", "design_score", "delivery_score", "options"]
#label_feature = ["like"]
#feature_names = str_features + int_features + label_feature

#train = train[feature_names]
#test = test[feature_names]
#val = val[feature_names]
#cached_train, vocabularies = DCN(train, str_features, int_features, df_type='train')
#cached_test = DCN(test, str_features, int_features, df_type = 'test')
#cached_val = DCN(val, str_features, int_features, df_type = 'test')
# save data
#with open('data/pickle/vocabularies.pickle','wb') as fw:
#    pickle.dump(vocabularies, fw)

# load data
#with open('data/pickle/vocabularies.pickle', 'rb') as fr:
#    vocabularies_loaded = pickle.load(fr)

#checkpoint_path2 = "data/model/thres_75.ckpt"
#checkpoint_dir2 = os.path.dirname(checkpoint_path2)

#learning_rate = 0.001
#model2 = model(cross_layer_sizes = 2,
#            deep_layer_sizes = [128, 64],
#            learning_rate = learning_rate,
#            vocabularies = vocabularies,
#            threshold = 0.75,
#            projection_dim = None,
#            metric = 'binary'
#            )

#model2.compile(optimizer = tf.keras.optimizers.Adam(learning_rate),
#              sample_weight_mode="temporal")

#callback = [tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3),
#            keras.callbacks.ModelCheckpoint(filepath=checkpoint_path2,
#                                            monitor='val_binary_accuracy',
#                                            save_best_only=True,
#                                            save_weights_only=True)]

#history= model2.fit(cached_train,  epochs=200, verbose=True,
#                    callbacks=callback, validation_data = cached_val)
#model2.load_weights(checkpoint_path2)

w = Tk()
w.title('🧚‍반려가구 추천요정🧚‍')
#w.title('반려가구 추천요정')
# frame 위젯
topFrame = Frame(w, width=900, height=20)
middleFrame = Frame(w, width=900, height=405)
bottomFrame = Frame(w, width=900, height=400)
# 공통 글꼴
curFont = Font(family='나눔고딕', size=15)

# 이미지 불러오기
photo1 = PhotoImage(file='image/IMG_8983_s.png')

cat = IntVar()
def c1():
    cat.set(1)
    return cat


def c2():
    cat.set(2)
    return cat


def c3():
    cat.set(3)
    return cat


def c4():
    cat.set(4)
    return cat


def c5():
    cat.set(5)
    return cat


def c6():
    cat.set(6)
    return cat


def c0():
    cat.set(0)
    return cat


# 위젯 생성
lblTitle = Label(topFrame, text='✨‍운명의 가구를 찾아드립니다🔮‍', font=('나눔고딕', 20))  # , bg='yellow')
#lblTitle = Label(topFrame, text='운명의 가구를 찾아드립니다', font=('나눔고딕', 20))
lblImage = Label(middleFrame, image=photo1)
# 입력 위젯
lblsite = Label(bottomFrame, text='당신의 닉네임을 입력하세요', font=('나눔고딕', 20))
site_entry = Entry(bottomFrame, width=30)
lblorder = Label(bottomFrame, text='원하는 느낌의 가구를 선택해 주세요!', font=('나눔고딕', 20))
btn1 = Button(bottomFrame, text='🏡 #맥시멀리스트 #본가의향기 #엄마의향기 #6시내고향템', font=curFont, command=c1)
btn2 = Button(bottomFrame, text='👩‍👩‍👧‍👧 #동거템 #셰어하우스템 #가평펜션템', font=curFont, command=c2)
btn3 = Button(bottomFrame, text='🌿 #홈카페 #인스타갬성템 #빈티지', font=curFont, command=c3)
btn4 = Button(bottomFrame, text='🖥 #기본에충실한 #깔끔 #심플 #모던', font=curFont, command=c4)
btn5 = Button(bottomFrame, text='🧑‍🎓 #가성비템 #학생템 #공부방템', font=curFont, command=c5)
btn6 = Button(bottomFrame, text='🪵 #가격대비만족 #오래쓰자 #한번사서제대로', font=curFont, command=c6)
btn0 = Button(bottomFrame, text='🙅 ‍찾는 카테고리가 없다면 클릭해 주세요 🤷', font=curFont, command=c0)

result = StringVar()


# 이벤트 구현
def okClick():
    w1 = Tk()
    w1.geometry('1000x1000')
    #load model
    #checkpoint_path2 = "data/thres_75.ckpt"
    #with open('data/vocabularies.pickle', 'rb') as fr:
    #    vocabularies = pickle.load(fr)
    #learning_rate = 0.001
    #model2 = model(cross_layer_sizes=2,
    #               deep_layer_sizes=[128, 64],
    #               learning_rate=learning_rate,
    #               vocabularies=vocabularies,
    #               threshold=0.75,
    #               projection_dim=None,
    #               metric='binary'
    #               )

    #model2.compile(optimizer=tf.keras.optimizers.Adam(learning_rate),
    #               sample_weight_mode="temporal")
    #model2.load_weights(checkpoint_path2)

    #load_data
    #item_list = pd.read_csv("data/item_list.csv", encoding="utf-8-sig")
    #for_user = pd.read_csv("data/for_user_final_0204.csv", encoding="utf-8-sig")

    userID = site_entry.get()
    category = cat.get()
    #rec
    #df = recommendation1(userID=userID, category=category, model=model2, item_list=item_list, for_user=for_user)
    if userID == "꿀이사냥":
        df = pd.read_csv("data/rec_0_{0}.csv".format(str(category)), encoding = "utf-8-sig")
    else:
        df = pd.read_csv("data/rec_x_{0}.csv".format(str(category)), encoding = "utf-8-sig")

    #treeview
    frame = Frame(w1)
    frame.pack()

    tree = ttk.Treeview(frame, columns=tuple(range(4)), height=100, show="headings")
    tree.pack(side='left')
    tree.heading(0, text=df.columns[0], anchor="center")
    tree.heading(1, text=df.columns[1], anchor="center")
    tree.heading(2, text=df.columns[2], anchor="center")
    tree.heading(3, text=df.columns[3], anchor="center")

    tree.column(0, width=150, anchor="center")
    tree.column(1, width=150, anchor="center")
    tree.column(2, width=150, anchor="center")
    tree.column(3, width=150, anchor="center")
    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scroll.set)
    for val in np.array(df).tolist():
        tree.insert('', 'end', values=(val[0], val[1], val[2], int(val[3])))
    #label = Label(w, text="뾰로롱✨")
    #label.pack() # 테이블 항목 클릭시 click_item 호출

    #result.set(res)

    #print(result)
    #showinfo("추천 결과입니다", result.get())


# 저장 위젯  (이벤트 추가 >>   command=okClick )
savebtn = Button(bottomFrame, text='   입력    ', font=curFont, command=okClick)

# 위젯 배치
# site_entry.grid(row=0, column=3)
# lblsite.grid(row=0, column=0)
# lblorder.grid(row = 15, column = 3)
# btn1.grid(row = 30, column = 0)
# btn2.grid(row = 30, column = 3)
# btn3.grid(row = 40, column = 0)
# btn4.grid(row = 40, column = 5)
# btn5.grid(row = 50, column = 0)
# btn6.grid(row = 50, column = 5)
# btn0.grid(row = 60, column = 0)
# savebtn.grid(row=70, column=5)

lblsite.pack()
site_entry.pack()
lblorder.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn0.pack()
savebtn.pack()
lblImage.pack()
lblTitle.pack()

topFrame.pack()
middleFrame.pack()
bottomFrame.pack()
w.geometry('1000x1000')
w.mainloop()
