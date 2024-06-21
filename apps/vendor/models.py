from django.db import models


class Vendor(models.Model):
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

    SEGMENTS_CHOICES = [
        ("RAW_MATERIALS", "Matérias-Primas"),
        ("COMPONENTS_PARTS", "Componentes e Peças"),
        ("MANUFACTURING_SERVICES", "Serviços de Fabricação e Subcontratação"),
        ("EQUIPMENT_MACHINERY", "Equipamentos e Máquinas"),
        ("LOGISTICS_TRANSPORTATION", "Serviços de Logística e Transporte"),
        ("IT_TELECOM", "Tecnologia da Informação e Telecomunicações"),
        ("MRO", "Manutenção, Reparo e Operações (MRO)"),
        ("PROFESSIONAL_SERVICES", "Serviços Profissionais"),
        ("CONSUMER_PRODUCTS", "Produtos de Consumo"),
        ("ENERGY_UTILITIES", "Energia e Utilidades"),
        ("MARKETING_ADVERTISING", "Marketing e Publicidade"),
        ("OFFICE_SUPPLIES", "Materiais de Escritório e Suprimentos Gerais"),
    ]

    fancy_name = models.CharField(max_length=100, blank=True)
    vendor_representative = models.CharField(max_length=100, blank=True)
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
    contact = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True)
    cpf = models.CharField(max_length=14, unique=True, null=True)
    cnpj = models.CharField(max_length=18, unique=True, null=True)
    rg = models.CharField(max_length=20, unique=True, null=True)
    issuing_authority = models.CharField(max_length=100, blank=True)
    general_observations = models.TextField(blank=True)
    segment = models.CharField(choices=SEGMENTS_CHOICES, max_length=24)
    active = models.BooleanField(default=True, blank=False)
