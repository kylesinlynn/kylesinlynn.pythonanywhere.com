from django.db import models


class Profile(models.Model):
    title = models.CharField(
        name="title", max_length=255, help_text="Enter your website title", null=True
    )
    description = models.TextField(
        name="description",
        max_length=500,
        help_text="Enter your website description",
        null=True,
    )
    keywords = models.TextField(
        name="keywords",
        help_text="Enter search keywords seperated by comma (,)",
        null=True,
    )
    image = models.ImageField(
        name="profile_image",
        upload_to="imgs/",
        help_text="Upload your profile image",
        blank=True,
        null=True,
    )
    resume = models.CharField(
        name="resume_link",
        max_length=500,
        help_text="Enter your resume url",
        blank=True,
        null=True,
    )
    email = models.EmailField(
        name="email", max_length=255, help_text="Enter your email address", null=True
    )
    phone = models.CharField(
        name="phone", max_length=255, help_text="Enter your phone number", null=True
    )
    facebook = models.CharField(
        name="facebook_username",
        max_length=255,
        help_text="Enter your facebook username",
        null=True,
    )
    x = models.CharField(
        name="x_username", max_length=255, help_text="Enter your X username", null=True
    )
    github = models.CharField(
        name="github_username",
        max_length=255,
        help_text="Enter your GitHub username",
        null=True,
    )

    def __str__(self) -> str:
        return self.title


class Work(models.Model):
    client = models.CharField(
        name="client",
        max_length=255,
        help_text="Enter your client name",
        blank=True,
        null=True,
    )
    title = models.CharField(
        name="title",
        max_length=255,
        help_text="Enter project name",
        blank=True,
        null=True,
    )
    description = models.TextField(
        name="description",
        max_length=500,
        help_text="Enter the details of the project",
        blank=True,
        null=True,
    )
    link = models.CharField(
        name="link",
        help_text="Enter project link",
        max_length=500,
        blank=True,
        null=True,
    )

    profile = models.ForeignKey(
        Profile, related_name="work", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.title
