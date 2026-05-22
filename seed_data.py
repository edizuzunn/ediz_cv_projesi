import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ediz_cv_projesi.settings')
django.setup()

from contact.models import Experience, Education, Skill, Project, Language

# Experiences
if Experience.objects.count() == 0:
    Experience.objects.create(
        title='Frontend Developer Intern',
        company='Jotform',
        date_range='Ağu 2025 - Eyl 2025 · Ankara',
        description='Contributed to the development of Jotform AI Chatbot, a new product integration for Canva. Built with React.js.',
        icon='icon-screen-desktop',
        order=1
    )
    Experience.objects.create(
        title='Frontend Developer Intern',
        company='SmartICT Bilişim A.Ş.',
        date_range='Tem 2025 - Ağu 2025 · Ankara',
        description='Actively participated in frontend development processes. Contributed to the development of dynamic web applications with React.js.',
        icon='icon-screen-tablet',
        order=2
    )
    print("✅ Experiences eklendi!")

# Education
if Education.objects.count() == 0:
    Education.objects.create(
        school='Piri Reis Üniversitesi',
        department='Bilişim Sistemleri Mühendisliği (İngilizce)',
        date_range='Eki 2022 - Haz 2027 · Lisans Derecesi',
        skills='Python, Deep Learning',
        order=1
    )
    print("✅ Education eklendi!")

# Skills
if Skill.objects.count() == 0:
    Skill.objects.create(name='Python', percentage=85, order=1)
    Skill.objects.create(name='React.js', percentage=80, order=2)
    Skill.objects.create(name='Django', percentage=75, order=3)
    Skill.objects.create(name='HTML5/CSS3', percentage=85, order=4)
    Skill.objects.create(name='Deep Learning', percentage=60, order=5)
    print("✅ Skills eklendi!")

# Projects
if Project.objects.count() == 0:
    Project.objects.create(
        title='League Point Table Calculator',
        description='A calculator for league point tables. Built to manage and calculate standings for sports leagues.',
        github_url='https://github.com/edizuzunn/League-Point-Table-Calculator',
        icon='icon-trophy',
        order=1
    )
    Project.objects.create(
        title='Specific Language Translation',
        description='A language translation tool for specific language pairs. Built with modern web technologies.',
        github_url='https://github.com/edizuzunn/Specific-Language-Translation',
        icon='icon-globe',
        order=2
    )
    print("✅ Projects eklendi!")

# Languages
if Language.objects.count() == 0:
    Language.objects.create(
        name='Türkçe',
        level='Ana dil',
        is_highlighted=False,
        icon='icon-speech',
        order=1
    )
    Language.objects.create(
        name='English',
        level='Professional Working Proficiency',
        is_highlighted=True,
        icon='icon-globe',
        order=2
    )
    print("✅ Languages eklendi!")

print("\n🎉 Tüm veriler başarıyla veritabanına yüklendi!")
