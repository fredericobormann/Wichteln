from django.db import models
from django.contrib.auth.models import User
from random import shuffle


class Party(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='party_owner', null=True)
    participants = models.ManyToManyField(User, related_name='party_participant')

    def __str__(self):
        return self.title

    def gen_donations(self):
        Donation.objects.filter(party=self).delete()
        party_participants = self.participants.all()
        shuffled_indices = list(range(len(party_participants)))
        shuffle(shuffled_indices)
        for i in range(len(party_participants)):
            donor = party_participants[shuffled_indices[i]]
            presentee = party_participants[shuffled_indices[(i+1) % len(party_participants)]]
            Donation.objects.create(party=self, donor=donor, presentee=presentee)
        return


class Donation(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name='donation')
    donor = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='donor', null=True)
    presentee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='presentee', null=True)

    def __str__(self):
        return f"{self.party.title}: {self.donor.username} gives to {self.presentee.username}"
