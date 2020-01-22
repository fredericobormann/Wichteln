from django.db import models
from django.contrib.auth.models import User


class Party(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='party_owner', null=True)
    participants = models.ManyToManyField(User, related_name='party_participant')

    def __str__(self):
        return self.title


class Donation(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='donation')
    donor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='donor', null=True)
    presentee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='presentee', null=True)

    def __str__(self):
        return f"{self.party.title}: {self.donor.username} gives to {self.presentee.username}"
