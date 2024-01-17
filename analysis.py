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
    recipes["breakfast"]={}
    recipes["lunch"]={}
    recipes["dinner"]={}
    recipes["addition"]={}

    ordered_fodata=order(fo_data)

    #早餐1,2,3
    bkf_1=random.choice(ordered_fodata["奶类及制品"])
    bkf_2=random.choice(ordered_fodata["蛋类、肉类及制品"])
    bkf_3=random.choice(ordered_fodata["蔬果和菌藻"])

    #午餐4,3,1,2
    lc_1=random.choice(ordered_fodata["蛋类、肉类及制品"])
    lc_2=random.choice(ordered_fodata["饮料"])
    lc_3=random.choice(ordered_fodata["谷薯芋、杂豆、主食"])
    lc_4_key=random.choice(list(ordered_fodata.keys()))
    while(lc_4_key=="蛋类、肉类及制品" or lc_4_key=="饮料" or lc_4_key=="谷薯芋、杂豆、主食" or lc_4_key=="食用油、油脂及制品" or lc_4_key=="零食、点心、冷饮" or lc_4_key=="坚果、大豆及制品"):
        lc_4_key=random.choice(list(ordered_fodata.keys()))
    lc_4=random.choice(ordered_fodata[lc_4_key])
    
    #晚餐4,3,1,2
    dn_1=random.choice(ordered_fodata["蛋类、肉类及制品"])
    dn_2=random.choice(ordered_fodata["饮料"])
    dn_3=random.choice(ordered_fodata["谷薯芋、杂豆、主食"])
    dn_4_key=random.choice(list(ordered_fodata.keys()))
    while(dn_4_key=="蛋类、肉类及制品" or dn_4_key=="饮料" or dn_4_key=="谷薯芋、杂豆、主食" or dn_4_key=="食用油、油脂及制品" or dn_4_key=="零食、点心、冷饮" or dn_4_key=="坚果、大豆及制品"):
        dn_4_key=random.choice(list(ordered_fodata.keys()))
    dn_4=random.choice(ordered_fodata[dn_4_key])
    
    #加餐
    ad_1=random.choice(ordered_fodata["零食、点心、冷饮"])

    #print(ordered_fodata.keys())
    #计算碳蛋脂日摄入量
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
    bft_cpf=[[bft_c*0.4,bft_p*0.4,bft_f*0.4],
             [bft_c*0.4,bft_p*0.4,bft_f*0.4],
             [bft_c*0.3,bft_p*0.3,bft_f*0.3],]

    lc_cpf=[[lc_c*0.2,lc_p*0.2,lc_f*0.2],
             [lc_c*0.1,lc_p*0.1,lc_f*0.1],
             [lc_c*0.4,lc_p*0.4,lc_f*0.4],
             [lc_c*0.3,lc_p*0.3,lc_f*0.3],]
    
    dn_cpf=[[dn_c*0.2,dn_p*0.2,dn_f*0.2],
             [dn_c*0.1,dn_p*0.1,dn_f*0.1],
             [dn_c*0.4,dn_p*0.4,dn_f*0.4],
             [dn_c*0.3,dn_p*0.3,dn_f*0.3],]
    


    #仅计算碳水和蛋白质
    recipes["breakfast"][bkf_1[0]]=min(bft_cpf[0][0]/float(bkf_1[3]),bft_cpf[0][1]/float(bkf_1[4]))
    if float(bkf_2[3])!=0:
        recipes["breakfast"][bkf_2[0]]=min(bft_cpf[1][0]/float(bkf_2[3]),bft_cpf[1][1]/float(bkf_2[4]))
    else:
        recipes["breakfast"][bkf_2[0]]=bft_cpf[1][1]/float(bkf_2[4])
    recipes["breakfast"][bkf_3[0]]=min(bft_cpf[2][0]/float(bkf_3[3]),bft_cpf[2][1]/float(bkf_3[4]))

    if float(lc_1[3])!=0:
        recipes["lunch"][lc_1[0]]=min(lc_cpf[0][0]/float(lc_1[3]),lc_cpf[0][1]/float(lc_1[4]))
    else:
        recipes["lunch"][lc_1[0]]=lc_cpf[0][1]/float(lc_1[4])

    if float(lc_2[3])!=0 and float(lc_2[4])!=0:
        recipes["lunch"][lc_2[0]]=min(lc_cpf[1][0]/float(lc_2[3]),lc_cpf[1][1]/float(lc_2[4]))
    else:
        recipes["lunch"][lc_2[0]]="适量"
    recipes["lunch"][lc_3[0]]=min(lc_cpf[2][0]/float(lc_3[3]),lc_cpf[2][1]/float(lc_3[4]))
    recipes["lunch"][lc_4[0]]=min(lc_cpf[3][0]/float(lc_4[3]),lc_cpf[3][1]/float(lc_4[4]))

    if float(dn_1[3])!=0:
        recipes["dinner"][dn_1[0]]=min(dn_cpf[0][0]/float(dn_1[3]),dn_cpf[0][1]/float(dn_1[4]))
    else:
        recipes["dinner"][dn_1[0]]=dn_cpf[0][1]/float(dn_1[4])
    
    if float(dn_2[3])!=0 and float(dn_2[4])!=0:
        recipes["dinner"][dn_2[0]]=min(dn_cpf[1][0]/float(dn_2[3]),dn_cpf[1][1]/float(dn_2[4]))
    else:
        recipes["dinner"][dn_2[0]]="适量"
    recipes["dinner"][dn_3[0]]=min(dn_cpf[2][0]/float(dn_3[3]),dn_cpf[2][1]/float(dn_3[4]))
    recipes["dinner"][dn_4[0]]=min(dn_cpf[3][0]/float(dn_4[3]),dn_cpf[3][1]/float(dn_4[4]))
    if float(ad_1[3])!=0 and float(ad_1[4])!=0:
        recipes["addition"][ad_1[0]]=min(ad_c/float(ad_1[3]),ad_p/float(ad_1[4]))
    else:
        recipes["addition"][ad_1[0]]="适量"
    return recipes

def make_recipes(fo_data):
    body_data=bmi_als()#包含身高，体重，身材类型
    recipes=analyze_recipes(fo_data,body_data)
    print("为您定制菜谱如下：")
    for key in recipes.keys():
        print(f"{key}",end="：\t")
        for food in recipes[key].keys():
            if(recipes[key][food]!="适量"):
                print(f"{food}：建议含量{recipes[key][food]*100:.2f}g",end="\n")
            else:
                print(f"{food}：适量",end="\n")
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
                for food in recipes[key].keys():
                    if(recipes[key][food]!="适量"):
                        print(f"{food}：建议含量{recipes[key][food]*100:.2f}g",end="\n")
                    else:
                        print(f"{food}：适量",end="\n")
                print("\n")
            satisfy=input("您对结果是否满意(Y/N)：")
        print("祝您饮食愉快！")
    else:
        print("输入错误，请重启")

    return recipes
    
if __name__=='__main__':
    fo_data=read.read_output()
    recipes=make_recipes(fo_data)  