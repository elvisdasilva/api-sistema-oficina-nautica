from django.db import models


class Customer(models.Model):
    STATE_CHOICES = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    ]

    GENDER_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
    ]

    STATUS_CHOICES = [
        ("AT", "Ativo"),
        ("IN", "Inativo"),
        ("PT", "Potencial"),
        ("CA", "Cancelado"),
        ("AN", "Análise"),
        ("EE", "Em espera"),
        ("VC", "Vencido"),
    ]

    REGISTRATION_TYPE_CHOICES = [
        ("PF", "Pessoa Física"),
        ("PJ", "Pessoa Jurídica"),
    ]

    full_name = models.CharField(max_length=100)
    fancy_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    address_complement = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES, max_length=2)
    zip_code = models.CharField(max_length=10, blank=True)
    first_telephone = models.CharField(max_length=20, blank=True)
    second_telephone = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    contato = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    date_of_birth = models.DateField(blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True)
    cnpj = models.CharField(max_length=18, unique=True, null=True)
    rg = models.CharField(max_length=20, unique=True, null=True)
    issuing_authority = models.CharField(max_length=100, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default="AT")
    general_observations = models.TextField(blank=True)
    registration_type = models.CharField(
        choices=REGISTRATION_TYPE_CHOICES, max_length=2
    )

    def __str__(self):
        return self.full_name
