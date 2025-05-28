import os
import shutil
import site

# الحصول على مسار site-packages
site_packages = site.getsitepackages()[0]

source_path = os.path.join(site_packages, "pinecone_client")
target_path = os.path.join(site_packages, "pinecone")

if not os.path.exists(source_path):
    print("❌ لم يتم العثور على pinecone_client. تأكد من أنك ثبتت pinecone-client==2.2.2")
elif os.path.exists(target_path):
    print("⚠️ مجلد pinecone موجود مسبقًا. احذفه يدويًا إذا كان تالفًا ثم أعد تشغيل السكربت.")
else:
    try:
        shutil.copytree(source_path, target_path)
        print(f"✅ تم إنشاء alias بنجاح: {target_path} → يشير إلى pinecone_client")
    except Exception as e:
        print(f"❌ خطأ أثناء النسخ: {e}")
