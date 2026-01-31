from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

import magic


ext_validator = FileExtensionValidator(['png', 'jpg', 'pdf'])

def validate_file_mimetype(file):
    print(file, file.__class__)
    accepted_exts: list = ['image/png', 'image/jpeg', 'application/pdf']

    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    print(file_mime_type)

    if file_mime_type not in accepted_exts:
        raise ValidationError("Unsupported file type.")
    

class CV(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    title = models.CharField(max_length=50)
    resume = models.FileField(upload_to="resumes/", validators=[ext_validator, validate_file_mimetype])

    def __str__(self) -> str:
        return f"{self.name} resume"
    
    def delete(self) -> None:
        self.resume.delete()
        super().delete()