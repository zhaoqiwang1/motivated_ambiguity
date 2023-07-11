from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'motivated_ambiguity'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
# 10 Choices for Eliciting Ambiguity Attitudes:
    Ambiguity_attitude_elicit1 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit2 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit3 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit4 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit5 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit6 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit7 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit8 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit9 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Ambiguity_attitude_elicit10 = models.StringField(
        choices=['Box K','Box U'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        '''
    )
    Guess_of_theta_color = models.IntegerField(
        label='''
        Here, you see your marked color (green or red), 
        please make a guess of the true value theta.
        '''
    )
    Guess_of_theta_signal = models.IntegerField(
        label='''
        Here, you can see your private signal, 
        your marked color is also by the side.
        Please make another guess of the true value theta.
        '''
    )
    Guess_of_sigma_signal = models.IntegerField(
        label='''
        In addition, please make another guess of the true sigma.
        '''
    )
# FUNCTIONS
# PAGES
class Task2(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1
    form_model = 'player'
    form_fields = ['Ambiguity_attitude_elicit1','Ambiguity_attitude_elicit2','Ambiguity_attitude_elicit3',     'Ambiguity_attitude_elicit4','Ambiguity_attitude_elicit5','Ambiguity_attitude_elicit6','Ambiguity_attitude_elicit7','Ambiguity_attitude_elicit8','Ambiguity_attitude_elicit9','Ambiguity_attitude_elicit10']


class Task3_color(Page):
        form_model = 'player'
        form_fields = ['Guess_of_theta_color']
        def vars_for_template(player):
             if player.participant.vars['ranking']==1:
                  color = 'green'
 #                 colorgreen = True
             else:
                  color = 'red'
 #                 colorgreen = False

             return {
                'Ambiguity_attitudes_elicit1': player.Ambiguity_attitude_elicit1,
                'ranking':player.participant.vars['ranking'],
                'color': color,
   #             'colorgreen':colorgreen,
         }
 

class Task3_priv_signal(Page):
    form_model = 'player'
    form_fields = ['Guess_of_theta_signal', 'Guess_of_sigma_signal']



page_sequence = [Task2, Task3_color, Task3_priv_signal]
