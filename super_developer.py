import os

def final_rockyou_upgrade(input_file, output_file):
    print("🛡️ جاري التنظيف والتطوير الشامل... انتظر النتائج المبهرة")
    
    # قائمة الإضافات الحديثة
    years = ['2025', '2026']
    symbols = ['!', '@', '#', '@2026']
    
    seen = set() # لمنع التكرار
    total_generated = 0

    try:
        with open(input_file, 'r', encoding='latin-1') as f_in, \
             open(output_file, 'w', encoding='utf-8') as f_out:
            
            for line in f_in:
                word = line.strip()
                
                # --- مرحلة التنظيف (Cleaning) ---
                # نتجاهل الكلمات القصيرة جداً (أقل من 6 حروف) لأنها غير مفيدة اليوم
                if len(word) < 6:
                    continue
                
                # --- مرحلة التضخيم (Expansion) ---
                # سنصنع "مجموعة" احتمالات للكلمة الواحدة
                variations = set()
                variations.add(word)            # الكلمة الأصلية
                variations.add(word.capitalize()) # أول حرف كبير
                variations.add(word.upper())      # كلها كبيرة
                
                # إضافة السنوات والرموز
                for yr in years:
                    variations.add(f"{word}{yr}")
                    variations.add(f"{word.capitalize()}{yr}")
                
                for sym in symbols:
                    variations.add(f"{word}{sym}")
                    variations.add(f"{word.capitalize()}{sym}")

                # كتابة النتائج في الملف الجديد مع منع التكرار
                for v in variations:
                    if v not in seen:
                        f_out.write(v + '\n')
                        seen.add(v)
                        total_generated += 1

                if total_generated % 500000 == 0:
                    print(f"🔄 وصلنا إلى {total_generated} كلمة في الملف الجديد...")

        print(f"✨ تم الانتهاء بنجاح!")
        print(f"📊 عدد الكلمات النهائي في القائمة المطورة: {total_generated}")
        print(f"📂 الملف جاهز باسم: {output_file}")

    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

# تشغيل المهمة
final_rockyou_upgrade('rockyou.txt', 'RockYou_Ultimate_2026.txt')