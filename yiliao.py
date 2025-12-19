# 第9章/yiliao.py
# 导入streamlit库，用于快速构建Web应用，简称为st（行业通用简写）
import streamlit as st
# 导入pickle库，用于序列化/反序列化Python对象（这里用来加载训练好的模型）
import pickle
# 导入pandas库，用于数据处理和分析，简称为pd（行业通用简写）
import pandas as pd

def introduce_page():
    """当选择简介页面时，将呈现该函数的内容"""
    # 在页面主区域输出一级标题：欢迎使用！
    st.write("# 欢迎使用！")
    
    # 在侧边栏输出提示文本，并设置成功样式（绿色背景）
    st.sidebar.success("单击💡 预测医疗费用")
    
    # 使用markdown语法输出富文本内容（支持标题、列表、链接等格式）
    st.markdown(
        """
        # 医疗费用预测应用💡
        这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。
        
        ## 背景介绍
        - 开发目标：帮助保险公司合理定价保险产品，控制风险。
        - 模型算法：利用随机森林回归算法训练医疗费用预测模型。
        
        ## 使用指南
        - 输入准确完整的被保险人信息，可以得到更准确的费用预测。
        - 预测结果可以作为保险定价的重要参考，但需审慎决策。
        - 有任何问题欢迎联系我们的技术支持。
        
        技术支持:email:: support@example.com
        """
    )

def predict_page():
    """当选择预测费用页面时，将呈现该函数的内容"""
    # 使用markdown语法输出预测页面的使用说明
    st.markdown(
        """
        ## 使用说明
        这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。
        - . **输入信息**：在下面输入被保险人的个人信息、疾病信息等。
        - . **费用预测**：应用会预测被保险人的未来医疗费用支出。
        """
    )
    
    # 创建一个表单容器，所有输入组件放入其中，需点击提交按钮才会触发提交
    with st.form('user_inputs'):
        # 创建数字输入框，用于输入年龄，最小值为0（默认无最大值）
        age = st.number_input('年龄', min_value=0)
        # 创建单选按钮，用于选择性别，选项为['男性', '女性']
        sex = st.radio('性别', options=['男性', '女性'])
        # 创建数字输入框，用于输入BMI（身体质量指数），最小值为0.0（浮点型）
        bmi = st.number_input('BMI', min_value=0.0)
        # 创建数字输入框，用于输入子女数量，步长为1（只能输入整数），最小值为0
        children = st.number_input('子女数量：', step=1, min_value=0)
        # 创建单选按钮，用于选择是否吸烟，选项为('是', '否')
        smoke = st.radio('是否吸烟', ('是', '否'))
        # 创建下拉选择框，用于选择区域，选项为('东南部', '西南部', '东北部', '西北部')
        region = st.selectbox('区域', ('东南部', '西南部', '东北部', '西北部'))
        # 创建表单提交按钮，按钮文字为'预测费用'，点击后会触发表单提交
        submitted = st.form_submit_button('预测费用')
    
    # 判断用户是否点击了提交按钮
    if submitted:
        # 将用户输入的原始数据临时存入列表（后续会替换为处理后的数据）
        format_data = [age, sex, bmi, children, smoke, region]
        
        # 初始化性别相关的哑变量（用于模型输入，因为模型无法直接识别文字）
        sex_female, sex_male = 0, 0
        # 根据用户选择的性别，设置对应的哑变量值（女性则sex_female=1，男性则sex_male=1）
        if sex == '女性':
            sex_female = 1
        elif sex == '男性':
            sex_male = 1
        
        # 初始化吸烟相关的哑变量
        smoke_yes, smoke_no = 0, 0
        # 根据用户选择的是否吸烟，设置对应的哑变量值（是则smoke_yes=1，否则smoke_no=1）
        if smoke == '是':
            smoke_yes = 1
        elif smoke == '否':
            smoke_no = 1
        
        # 初始化区域相关的哑变量
        region_northeast, region_southeast, region_northwest, region_southwest = 0, 0, 0, 0
        # 根据用户选择的区域，设置对应的哑变量值（选中哪个区域，对应变量=1）
        if region == '东北部':
            region_northeast = 1
        elif region == '东南部':
            region_southeast = 1
        elif region == '西北部':
            region_northwest = 1
        elif region == '西南部':
            region_southwest = 1
        
        # 重新整理数据为模型可接受的格式（所有特征均为数值型哑变量）
        format_data = [age, bmi, children, sex_female, sex_male,
                       smoke_no, smoke_yes,
                       region_northeast, region_southeast, region_northwest, region_southwest]
        
        # 以二进制只读模式打开预训练的随机森林回归模型文件（rfr_model.pkl）
        with open('rfr_model.pkl', 'rb') as f:
            # 使用pickle.load反序列化加载模型对象到内存
            rfr_model = pickle.load(f)
        
        # 将处理后的数值型数据转换为DataFrame（模型要求输入格式为DataFrame）
        # columns=rfr_model.feature_names_in_ 确保列名与模型训练时的列名完全一致
        format_data_df = pd.DataFrame(data=[format_data], columns=rfr_model.feature_names_in_)
        # 使用加载的模型对输入数据进行预测，[0]取预测结果的第一个值（因为预测结果是数组）
        predict_result = rfr_model.predict(format_data_df)[0]
        
        # 在页面输出预测结果，round(predict_result, 2)将结果保留2位小数
        st.write('根据您输入的数据，预测该客户的医疗费用是：', round(predict_result, 2))
        # 输出技术支持联系方式
        st.write("技术支持:email:: support@example.com")

# 设置Streamlit页面的配置：标题为"医疗费用预测"，页面图标为💡
st.set_page_config(
    page_title="医疗费用预测",
    page_icon="💡",
)

# 在侧边栏创建单选按钮导航栏，选项为["简介", "预测医疗费用"]，选中的值存入变量nav
nav = st.sidebar.radio("导航", ["简介", "预测医疗费用"])
# 根据用户选择的导航选项，执行对应的函数
if nav == "简介":
    introduce_page()
else:
    predict_page()