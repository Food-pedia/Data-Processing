import os
first_path_xml = r"C:\Users\esthe\OneDrive\바탕 화면\졸프데이터\ConvertVOC\ConvertVOC"
first_path_img = r"C:\Users\esthe\OneDrive\바탕 화면\졸프데이터\정리된이미지"

#식품 목록 추출
xmlFood_list= os.listdir(first_path_xml) 
imgFood_list= os.listdir(first_path_img)

selectedXmlFood_list=[]
selectedImgFood_list=[]
for x in xmlFood_list:
    name = x+"_완"
    if name in imgFood_list:
        selectedXmlFood_list.append(x)

# 식품별 이미지 정리        
for i in selectedXmlFood_list:
    print(i)
    for k in range(0,2):
        path_xml = first_path_xml + "\\" + i
        path_img = first_path_img + "\\" + i + "_완"
    
        # 1: xml의 파일 이름 추출
        xmlFile_list= os.listdir(path_xml)
        xmlFile_names=[]
        for x in xmlFile_list:
            name = x.split('.')[0]
            xmlFile_names.append(name)

        # 2: img 파일에서 .이 2개인 파일 삭제
        imgFile_list= os.listdir(path_img)
        imgFile_names=[]
        for x in imgFile_list:
            if x.count('Img') == 1:
                if x.count('.') != 1:
                    if os.path.exists(path_img + "\\" + x):
                        os.remove(path_img + "\\" + x)
                        break
                else: # 3: img 파일 이름 추출 및 확장자 jpg로 변경
                    name = x.split('.')[0]
                    imgFile_names.append(name)
                    if x.split('.')[1] != 'jpg':
                        os.rename(path_img + "\\" + x, path_img + "\\" + name + '.jpg')
        
        # 4: 차집합으로 삭제해야 할 img 파일 이름 추출
        differ = set(imgFile_names) - set(xmlFile_names)
        a = tuple(differ)
        res = sorted(a, key=lambda x: (lambda y: (int(y[2]), int(y[1]), y[0]))(x.split('_')))
        print(res)
        
        # 5: img 파일 삭제
        for file in res:
            if os.path.exists(path_img + "\\" + file + '.jpg'):
                os.remove(path_img + "\\" + file + '.jpg')
        print('삭제 완료')

#떡국은 이름이 달라서 따로 삭제
for i in range (0,20):

    path_xml = r"C:\Users\esthe\OneDrive\바탕 화면\졸프데이터\ConvertVOC\ConvertVOC\떡국"
    path_img = r"C:\Users\esthe\OneDrive\바탕 화면\졸프데이터\새 폴더\떡국_만두국_완"

    xmlFile_list= os.listdir(path_xml)
    xmlFile_names=[]
    for x in xmlFile_list:
        name = x.split('.')[0]
        xmlFile_names.append(name)
    print(xmlFile_names, len(xmlFile_names))

    imgFile_list= os.listdir(path_img)
    imgFile_names=[]
    for x in imgFile_list:
        if x.count('Img') == 1:
            if x.count('.') != 1:
                if os.path.exists(path_img + "\\" + x):
                    os.remove(path_img + "\\" + x)
                    break
            else:
                name = x.split('.')[0]
                imgFile_names.append(name)
                if x.split('.')[1] != 'jpg':
                    os.rename(path_img + "\\" + x, path_img + "\\" + name + '.jpg')

    print(imgFile_names, len(imgFile_names))

    differ = set(imgFile_names) - set(xmlFile_names)
    a = tuple(differ)
    res = sorted(a, key=lambda x: (lambda y: (int(y[2]), int(y[1]), y[0]))(x.split('_')))
    print(res)

    for file in res:
        if os.path.exists(path_img + "\\" + file + '.jpg'):
            os.remove(path_img + "\\" + file + '.jpg')
    print('삭제 완료')

#식품별로 이미지 파일 안에 xml 파일 이동
for i in selectedXmlFood_list:
    print(i)
    path_xml = first_path_xml + "\\" + i
    path_img = first_path_img + "\\" + i + "_완"
    xmlFile_list = os.listdir(path_xml)
    for file in xmlFile_list:
        os.rename(path_xml+"\\"+file, path_img+"\\"+file)

#식품별 번호 확인
for i in selectedXmlFood_list:
    print(i)
    path_xml = first_path_xml + "\\" + i
    path_img = first_path_img + "\\" + i + "_완"
    imgFile_list = os.listdir(path_img)
    print(imgFile_list[3])