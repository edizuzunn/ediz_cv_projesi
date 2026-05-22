from django.db import models


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date'
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date'
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='This is variable of the setting.',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )

    def __str__(self):
        return f'General Setting: {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ContactMessage(AbstractModel):
    name = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Name',
    )
    email = models.EmailField(
        max_length=254,
        blank=True,
        verbose_name='Email',
    )
    subject = models.CharField(
        max_length=254,
        blank=True,
        verbose_name='Subject',
    )
    message = models.TextField(
        blank=True,
        verbose_name='Message',
    )

    def __str__(self):
        return f'Message from {self.name} - {self.subject}'

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ('-created_date',)


class Experience(AbstractModel):
    title = models.CharField(max_length=254, verbose_name='Job Title')
    company = models.CharField(max_length=254, verbose_name='Company')
    date_range = models.CharField(max_length=254, verbose_name='Date Range', help_text='e.g. Ağu 2025 - Eyl 2025 · Ankara')
    description = models.TextField(verbose_name='Description')
    icon = models.CharField(max_length=100, default='icon-screen-desktop', verbose_name='Icon Class', help_text='e.g. icon-screen-desktop, icon-screen-tablet')
    order = models.IntegerField(default=0, verbose_name='Display Order')

    def __str__(self):
        return f'{self.title} - {self.company}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('order',)


class Education(AbstractModel):
    school = models.CharField(max_length=254, verbose_name='School Name')
    department = models.CharField(max_length=254, verbose_name='Department')
    date_range = models.CharField(max_length=254, verbose_name='Date Range', help_text='e.g. Eki 2022 - Haz 2027 · Lisans Derecesi')
    skills = models.CharField(max_length=254, blank=True, verbose_name='Skills', help_text='e.g. Python, Deep Learning')
    order = models.IntegerField(default=0, verbose_name='Display Order')

    def __str__(self):
        return f'{self.school} - {self.department}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('order',)


class Skill(AbstractModel):
    name = models.CharField(max_length=254, verbose_name='Skill Name')
    percentage = models.IntegerField(default=50, verbose_name='Percentage', help_text='0-100 arası bir değer girin')
    order = models.IntegerField(default=0, verbose_name='Display Order')

    def __str__(self):
        return f'{self.name} - {self.percentage}%'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)


class Project(AbstractModel):
    title = models.CharField(max_length=254, verbose_name='Project Title')
    description = models.TextField(verbose_name='Description')
    github_url = models.URLField(max_length=500, blank=True, verbose_name='GitHub URL')
    icon = models.CharField(max_length=100, default='icon-trophy', verbose_name='Icon Class', help_text='e.g. icon-trophy, icon-globe, icon-energy')
    order = models.IntegerField(default=0, verbose_name='Display Order')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('order',)


class Language(AbstractModel):
    name = models.CharField(max_length=254, verbose_name='Language')
    level = models.CharField(max_length=254, verbose_name='Proficiency Level', help_text='e.g. Ana dil, Professional Working Proficiency')
    is_highlighted = models.BooleanField(default=False, verbose_name='Highlighted?', help_text='Mavi arka planla vurgulanacak mı?')
    icon = models.CharField(max_length=100, default='icon-speech', verbose_name='Icon Class', help_text='e.g. icon-speech, icon-globe')
    order = models.IntegerField(default=0, verbose_name='Display Order')

    def __str__(self):
        return f'{self.name} - {self.level}'

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ('order',)
