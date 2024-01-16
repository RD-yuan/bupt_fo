import openpyxl
import read 
import random

#-2,-1,0,1分别代表肥胖，超重，正常，偏瘦
def bmi_als():
    height=int(input("请输入身高（cm）："))
    weight=int(input("请输入体重（kg）："))
    bmi = weight/height/height*10000
    print("您的bmi为{:.2f}".format(bmi))

    body_type_list=["偏瘦","正常","超重","肥胖"]

    if bmi < 18.5:
        body_type = -1
    elif bmi<24:
        body_type=0
    elif bmi<28:
        body_type=1
    else:
        body_type=2

    print(f"您的体重类型为{body_type_list[body_type+1]}")
    body_data=[height,weight,body_type]
    return body_data

def order(fo_data):
    ordered_fodata={}#用字典匹配食物类别和食物元素
    for food in fo_data[1:]:
        fo_type=food[1]
        if fo_type not in ordered_fodata.keys():
            ordered_fodata[fo_type]=[food,]
        else:
            ordered_fodata[fo_type].append(food)

    return ordered_fodata

#进行一个简单的食谱匹配，根据
def analyze_recipes(fo_data,body_data):
    recipes={}
    recipes["breakfast"]=[]
    recipes["lunch"]=[]
    recipes["dinner"]=[]
    recipes["addition"]=[]

    ordered_fodata=order(fo_data)

    #1,2,3
    bkf_1=random.choice(ordered_fodata["奶类及制品"])
    bkf_2=random.choice(ordered_fodata["蛋类、肉类及制品"])
    bkf_3=random.choice(ordered_fodata["蔬果和菌藻"])

    #4,3,1,2
    lc_1=random.choice(ordered_fodata["蛋类、肉类及制品"])
    lc_2=random.choice(ordered_fodata["饮料"])
    lc_3=random.choice(ordered_fodata["谷薯芋、杂豆、主食"])
    lc_4_key=random.choice(list(ordered_fodata.keys()))
    while(lc_4_key=="蛋类、肉类及制品" or lc_4_key=="饮料" or lc_4_key=="谷薯芋、杂豆、主食" or lc_4_key=="食用油、油脂及制品" or lc_4_key=="零食、点心、冷饮" or lc_4_key=="坚果、大豆及制品"):
        lc_4_key=random.choice(list(ordered_fodata.keys()))
    lc_4=random.choice(ordered_fodata[lc_4_key])
    
    #4,3,1,2
    dn_1=random.choice(ordered_fodata["蛋类、肉类及制品"])
    dn_2=random.choice(ordered_fodata["饮料"])
    dn_3=random.choice(ordered_fodata["谷薯芋、杂豆、主食"])
    dn_4_key=random.choice(list(ordered_fodata.keys()))
    while(dn_4_key=="蛋类、肉类及制品" or dn_4_key=="饮料" or dn_4_key=="谷薯芋、杂豆、主食" or dn_4_key=="食用油、油脂及制品" or dn_4_key=="零食、点心、冷饮" or dn_4_key=="坚果、大豆及制品"):
        dn_4_key=random.choice(list(ordered_fodata.keys()))
    dn_4=random.choice(ordered_fodata[dn_4_key])
    
    ad_1=random.choice(ordered_fodata["零食、点心、冷饮"])

    #print(ordered_fodata.keys())
    if body_data[2]==-2:
        #肥胖人群——低碳脂食谱
        carbon=body_data[1]*1.7
        protain=body_data[1]*1.1
        fat=body_data[1]*0.6
    elif body_data[2]==-1:
        #超重人群——低碳食谱
        carbon=body_data[1]*1.8
        protain=body_data[1]*1.2
        fat=body_data[1]*0.8
    elif body_data[2]==0:
        #正常人群——随机食谱
        carbon=body_data[1]*2.0
        protain=body_data[1]*1.3
        fat=body_data[1]*1.2
    else:
        #偏瘦人群——增碳蛋脂食谱
        carbon=body_data[1]*2.2
        protain=body_data[1]*1.5
        fat=body_data[1]*1.2

    bft_c=carbon*0.25
    bft_p=protain*0.25
    bft_f=fat*0.25

    lc_c=carbon*0.35
    lc_p=protain*0.35
    lc_f=fat*0.35

    dn_c=carbon*0.30
    dn_p=protain*0.30
    dn_f=fat*0.30

    ad_c=carbon*0.10
    ad_p=protain*0.10
    ad_f=fat*0.10

    #针对不同食物的数据设定食谱含量

    recipes["breakfast"].append(bkf_1[0])
    recipes["breakfast"].append(bkf_2[0])
    recipes["breakfast"].append(bkf_3[0])

    recipes["lunch"].append(lc_1[0])
    recipes["lunch"].append(lc_2[0])
    recipes["lunch"].append(lc_3[0])
    recipes["lunch"].append(lc_4[0])

    recipes["dinner"].append(dn_1[0])
    recipes["dinner"].append(dn_2[0])
    recipes["dinner"].append(dn_3[0])
    recipes["dinner"].append(dn_4[0])

    recipes["addition"].append(ad_1[0])


    return recipes

def make_recipes(fo_data):
    body_data=bmi_als()#包含身高，体重，身材类型
    recipes=analyze_recipes(fo_data,body_data)
    print("为您定制菜谱如下：")
    for key in recipes.keys():
        print(f"{key}",end="：\t")
        for item in recipes[key]:
            print(item,end="\t")
        print("\n")
    satisfy=input("您对结果是否满意(Y/N)：")
    if(satisfy=="Y"):
        print("祝您饮食愉快！")
    elif satisfy=="N":
        while(satisfy=="N"):
            print("为您重新定制菜谱：")
            recipes=analyze_recipes(fo_data,body_data)
            for key in recipes.keys():
                print(f"{key}",end="：\t")
                for item in recipes[key]:
                    print(item,end="\t")
                print("\n")
            satisfy=input("您对结果是否满意(Y/N)：")
    else:
        print("输入错误，请重启")

    return recipes
    
if __name__=='__main__':
    fo_data=read.read_output()
    recipes=make_recipes(fo_data)  