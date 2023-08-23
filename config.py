# 公众号配置
# 公众号appId
app_id = "wx6ab129f6f29ec5f2"
# 公众号appSecret
app_secret = "35784526f9f23fb8f777d6bc2ec1f891"
# 模板消息id
# 每日消息
template_id1 = "F4n0qca_doVggeMfmmXG584nuJFHMaiek65nkkSLzPA"
# 课程消息,上课提醒
template_id2 = "wBpOANViDXjsD1vWx0P1RakvHz_yASxnr7sKUyMkCr4"
# 晚安心语
template_id3 = "9sGqU0AvgHmTCIvh3xxvVKHfP_3PE5e5qlca4oLN1kg"
# 接收公众号消息的微信号
# 这是openid
user = ["oIe2Z5r7lNZ4PsBKNcNICa63t8t0"]
# xx  "oIe2Z5r7lNZ4PsBKNcNICa63t8t0"
# hh  "oIe2Z5qmxK8xuhgv2PzlRfLjCzuI"
# 信息配置
# 所在省份
province = "河北"
# 所在城市
city = "张家口"
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1，---------倒计时
birthday = "2002-7-2"
# 在一起的日子，格式同上------------计时器
love_date = "2019-10-30"
# 天行数据晚安心语 key
good_Night_Key = "16cb62d9c27a25b5be8d63a1b9164e2f"
# -------------------------------------------------------------------------
# 设置学期第一周开始日期
year = 2023
month = 8
day = 21
# 每日推送时间
post_Time = "07:35:00"
# 每节课提醒时间（有课才会提醒）, 时:分:秒  的形式, 字符串, 根据个人需要设置几次
time_table = ["08:04:00", "10:10:00", "14:04:00", "16:04:00"]
# 课程时间
course_Time = ["8:30--10：10", "10:20--12：00", "14:30--16：10", "16:20--18：00"]
# 晚安心语及第二天课程推送时间
good_Night_Time = "23:20:00"
# 课程表 "1"代表第一周，依次类推，根据个人实际课表添加，有几周就添加几周,
# 每一行代表一天, 例如  ['', '编译原理', '', '数据库原理及应用', '数据分析原理', '']  代表周一
classes = \
    {
        "1": [
            ['西医内科学', '康复医学', '', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "2": [
            ['西医内科学', '康复医学', '', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "3": [
            ['西医内科学', '康复医学', '', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "4": [
            ['西医内科学', '康复医学', '', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "5": [
            ['西医内科学', '康复医学', '西医内科学（实践）', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医眼科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "6": [
            ['西医内科学', '康复医学', '西医内科学（实践）', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医眼科学（实践）', '中药学', '', '', '', ''],
            ['', '中药学', '', '', '', '']
        ],
        "7": [
            ['西医内科学', '康复医学', '西医内科学（实践）', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医眼科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "8": [
            ['西医内科学', '康复医学', '西医内科学（实践）', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医眼科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "9": [
            ['西医内科学', '康复医学', '西医内科学（实践）', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '老年病学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医眼科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "10": [
            ['西医内科学', '康复医学', '西医内科学（实践）', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '老年病学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医眼科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
        "11": [
            ['西医内科学', '康复医学', '医学影像学', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '老年病学（理论）', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医妇科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
         "12": [
            ['西医内科学', '康复医学', '医学影像学', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）+老年病学', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医妇科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
         "13": [
            ['西医内科学', '康复医学', '医学影像学', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）+老年病学', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医妇科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
         "14": [
            ['西医内科学', '康复医学', '医学影像学', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）+老年病学', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医妇科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
         "15": [
            ['西医内科学', '康复医学', '医学影像学', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）+老年病学', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医妇科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ],
         "16": [
            ['西医内科学', '康复医学', '医学影像学', '', '', ''],
            ['中医内科学（理论+实践）', '中医外科学', '中医眼科学', '', '', ''],
            ['中医内科学', '中医儿科学（理论）+老年病学', '老年病学', '', '', ''],
            ['医学影像学', '西医内科学', '康复医学实训', '', '', ''],
            ['中医儿科学', '中医妇科学（理论）', '', '', '', ''],
            ['中医妇科学（实践）', '中药学', '', '', '', ''],
            ['', '', '', '', '', '']
        ]
    }



# 模板 1：每日提醒模板
# 本周是开学的第: {{weeks.DATA}} 周
# 今天是: {{date.DATA}}
# 城市： {{city.DATA}}
# 天气： {{weather.DATA}}
# 最低气温: {{min_temperature.DATA}}
# 最高气温: {{max_temperature.DATA}}
# 今天是破壳日的第: {{love_day.DATA}} 天
# 距离开学还有: {{birthday.DATA}} 天
# ----------------今日课程----------------
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}

# 模板 2 课程单推
# 课程信息: {{classInfo.DATA}}

# 模板 3 晚安心语推送和第二天课程推送
# {{goodNight.DATA}}
# ----------------明日课程----------------
# 明天是: {{week.DATA}}
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}
