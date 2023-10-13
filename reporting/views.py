from django.shortcuts import render

projects =[
{ 'id' :13, 'recipient': 'CP2011' , 'project_name': 'وحدة التفحيم' , 'finish_date': '2026/12/31'},
{ 'id' :2, 'recipient': 'CP3021' , 'project_name': 'مستودعات المازوت' , 'finish_date': '2023/06/30'},
{ 'id' :3, 'recipient': 'CP3022' , 'project_name': 'مستودعات البنزين' , 'finish_date': '2023/07/30'},
{ 'id' :4, 'recipient': 'CP3025' , 'project_name': 'مازوت م13' , 'finish_date': '2023/09/30'},
{ 'id' :5, 'recipient': 'CP3024' , 'project_name': 'المستودعات الكروية' , 'finish_date': '2023/09/30'},
{ 'id' :6, 'recipient': 'C53003' , 'project_name': 'محطة الصرف الصناعي - شركة السويس' , 'finish_date': '2024/04/30'},
{ 'id' :7, 'recipient': 'CP2015' , 'project_name': 'مستودعات التفحيم' , 'finish_date': '2023/12/31'},
{ 'id' :8, 'recipient': 'CP2017' , 'project_name': 'مازوت م14' , 'finish_date': '2024/12/31'},
{ 'id' :9, 'recipient': 'CK2029' , 'project_name': 'مستودعات الدفع' , 'finish_date': '2024/05/15'},
{ 'id' :10, 'recipient': 'C62017' , 'project_name': 'تشغيل وحدة الاسفلت' , 'finish_date': '2024/04/01'},
{ 'id' :11, 'recipient': 'C62018' , 'project_name': 'اعادة تأهيل المنطقة الشمالية' , 'finish_date': '2025/12/30'},
{ 'id' :12, 'recipient': 'CW3001' , 'project_name': 'محطة الكهرباء' , 'finish_date': '2024/12/30'},
{ 'id' :14, 'recipient': 'CP3029' , 'project_name': 'اتفاقية خدمات النصر' , 'finish_date': '2023/11/26'},
{ 'id' :15, 'recipient': 'CP1014' , 'project_name': 'VRU' , 'finish_date': '2024/06/30'},
{ 'id' :16, 'recipient': 'CI1003' , 'project_name': 'معالجة مياه البحر - النصر' , 'finish_date': '2024/06/25'},
{ 'id' :17, 'recipient': 'CP3023' , 'project_name': 'توسعات محطة الانابيب' , 'finish_date': '2024/01/31'},
{ 'id' :18, 'recipient': 'CK3020' , 'project_name': 'مستودع التعاون' , 'finish_date': '2024/03/31'},
{ 'id' :19, 'recipient': 'C61007' , 'project_name': 'غرف بلوف الانابيب' , 'finish_date': '2024/02/28'},
{ 'id' :20, 'recipient': 'W12002' , 'project_name': 'رصيف ميناء السخنة' , 'finish_date': '2023/12/29'},
{ 'id' :21, 'recipient': 'CK3022' , 'project_name': 'تطوير شبكة حريق' , 'finish_date': '2023/12/31'},
{ 'id' :22, 'recipient': 'C52001' , 'project_name': 'محطة الصرف الصناعي - الشركة العامة' , 'finish_date': '2023/12/31'},
{ 'id' :23, 'recipient': 'CK3021' , 'project_name': 'توسعات محطة الحمد' , 'finish_date': '2024/12/31'},
{ 'id' :24, 'recipient': 'CL3293' , 'project_name': 'خط وادي حجول' , 'finish_date': '2024/12/31'},
{ 'id' :25, 'recipient': 'CL3311' , 'project_name': 'خط جابكو' , 'finish_date': '2023/09/30'},
{ 'id' :26, 'recipient': 'C13101' , 'project_name': 'خط الرسوة بورسعيد' , 'finish_date': '2024/07/17'},
{ 'id' :27, 'recipient': 'W13103' , 'project_name': 'محطة الخلط المركزية' , 'finish_date': '2023/12/31'},
{ 'id' :28, 'recipient': 'CS3030' , 'project_name': 'المبنى الادارى للانابيب' , 'finish_date': '2023/12/31'},
{ 'id' :29, 'recipient': 'W13104' , 'project_name': 'طريق السويس السخنة' , 'finish_date': '2023/10/31'},
{ 'id' :30, 'recipient': 'C12019' , 'project_name': 'تطوير رصيف ميناء جبل الزيت' , 'finish_date': '2023/11/30'},
{ 'id' :31, 'recipient': 'C13129' , 'project_name': 'القطار فائق السرعة' , 'finish_date': '2023/11/30'},
{ 'id' :32, 'recipient': 'CB3002' , 'project_name': 'انشاء كبارى LRT' , 'finish_date': '2024/06/30'},
{ 'id' :33, 'recipient': 'CL3328' , 'project_name': 'خط العريش' , 'finish_date': '2024/01/31'},
{ 'id' :34, 'recipient': 'CK5112' , 'project_name': 'مستودعات بتروبل ' , 'finish_date': '2023/06/30'},
{ 'id' :35, 'recipient': 'CL3323' , 'project_name': 'خطوط الحوض السادس' , 'finish_date': '2024/04/27'},
{ 'id' :36, 'recipient': 'C13140' , 'project_name': 'سور ارض  السماد' , 'finish_date': '2023/10/31'},
{ 'id' :37, 'recipient': 'CC2003' , 'project_name': 'مجمع البتروكيماويات' , 'finish_date': '2024/02/29'},
{ 'id' :38, 'recipient': 'C52002' , 'project_name': 'محطة الصرف الصناعي - سوكو' , 'finish_date': '2023/06/30'},
{ 'id' :39, 'recipient': 'CK2014' , 'project_name': 'مستودعات عجرود' , 'finish_date': '2023/11/30'},
{ 'id' :40, 'recipient': 'CL3276' , 'project_name': 'خط رأس بدران' , 'finish_date': '2023/09/30'},
{ 'id' :41, 'recipient': 'CF2317' , 'project_name': 'برج التقطير' , 'finish_date': '2023/12/31'},
{ 'id' :42, 'recipient': 'EW2001' , 'project_name': 'الطاقة الشمسية' , 'finish_date': '2024/06/10'},
{ 'id' :43, 'recipient': 'CL3337' , 'project_name': 'GRE' , 'finish_date': '2024/06/30'},
{ 'id' :44, 'recipient': 'CK5117' , 'project_name': 'تانك 21' , 'finish_date': '2024/10/31'},
{ 'id' :45, 'recipient': 'M43009' , 'project_name': 'معسكر رأس غارب' , 'finish_date': '2022/06/30'},
{ 'id' :46, 'recipient': 'M43010' , 'project_name': 'معسكر أبو رديس' , 'finish_date': '2022/12/31'},
{ 'id' :47, 'recipient': 'M43011' , 'project_name': 'معسكر جبل الزيت' , 'finish_date': '2023/12/31'},
{ 'id' :48, 'recipient': 'M43014' , 'project_name': 'معسكر سوميد' , 'finish_date': '2022/12/31'},
{ 'id' :49, 'recipient': 'M43015' , 'project_name': 'معسكر الصينية' , 'finish_date': '2023/08/31'},
{ 'id' :50, 'recipient': 'WL3018' , 'project_name': 'مدرسة اللحام' , 'finish_date': '2023/09/30'},
{ 'id' :52, 'recipient': 'CL3330' , 'project_name': 'تعديل اجزاء خطوط الانابيب' , 'finish_date': '2023/10/31'},
{ 'id' :53, 'recipient': 'CF1029' , 'project_name': 'انشاء مصنع التغليف' , 'finish_date': '2023/02/28'},
{ 'id' :54, 'recipient': 'CP1007' , 'project_name': 'DCU' , 'finish_date': '2023/12/31'},
{ 'id' :55, 'recipient': 'C13058' , 'project_name': 'رصيف ميناء دمياط' , 'finish_date': '2023/06/30'},
{ 'id' :56, 'recipient': 'C13080' , 'project_name': 'القطار الكهربائى' , 'finish_date': '2023/12/31'},
{ 'id' :57, 'recipient': 'CF2221' , 'project_name': 'مستودعات راس غارب' , 'finish_date': '2023/08/31'},
{ 'id' :58, 'recipient': 'C13086' , 'project_name': 'جراج الهيئة' , 'finish_date': '2023/07/31'},
{ 'id' :59, 'recipient': 'CK2031' , 'project_name': 'محطة الرسوة' , 'finish_date': '2025/12/31'},
{ 'id' :60, 'recipient': 'CL3299' , 'project_name': 'خطوط التعاون' , 'finish_date': '2023/08/31'},
{ 'id' :61, 'recipient': 'CC2001' , 'project_name': 'مجمع الاسمدة الازوتية' , 'finish_date': '2023/12/31'},
{ 'id' :62, 'recipient': 'CC3018' , 'project_name': 'مصنع الكلور' , 'finish_date': '2024/12/30'},
{ 'id' :63, 'recipient': 'CC3019' , 'project_name': 'مصنع الهيدروجين' , 'finish_date': '2024/04/27'},
]


def home (request):
  context = {"projects": projects}
  return render(request, 'home.html',context)

def project (request, pk):
  project = None
  for i in projects:
    if i['recipient'] == pk:
      project = i

  context = {"project": project}
  return render(request, 'project.html',context)

def login (request):
  return render(request, 'login.html')