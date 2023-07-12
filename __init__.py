from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'motivated_ambiguity'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


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
        ''')
    Guess_of_theta_signal = models.IntegerField(
        label='''
        Guess of theta
        ''')
    Guess_of_sigma_signal = models.IntegerField(
        label='''
        Guess of sigma
        ''')
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
            ############################################################
            # Below, we store predetermined color parameters in the 
            # following code. Parameters are round_number and iq_ranking
            # dependent. We can change them anytime.
            ############################################################
            ### Round 1 ###
             if player.round_number == 1:
              if player.participant.vars['ranking']== 1:
                  color = 'green'
              elif player.participant.vars['ranking']== 2:
                  color = 'green'
              elif player.participant.vars['ranking']== 3:
                  color = 'red'
              elif player.participant.vars['ranking']== 4:
                  color = 'red'
              else:
                  color = None
            ### Round 2 ###
             elif player.round_number == 2:
              if player.participant.vars['ranking']== 1:
                  color = 'green'
              elif player.participant.vars['ranking']== 3:
                  color = 'green'
              elif player.participant.vars['ranking']== 2:
                  color = 'red'
              elif player.participant.vars['ranking']== 4:
                  color = 'red'
              else:
                  color = None
            ### Round 3 ###
             else:
              if player.participant.vars['ranking']== 2:
                  color = 'green'
              elif player.participant.vars['ranking']== 4:
                  color = 'green'
              elif player.participant.vars['ranking']== 1:
                  color = 'red'
              elif player.participant.vars['ranking']== 3:
                  color = 'red'
              else:
                  color = None

             return {
 #               'Ambiguity_attitude_elicit1': player.Ambiguity_attitude_elicit1,
                'ranking':player.participant.vars['ranking'],
                'color': color,
   #             'colorgreen':colorgreen,
           }
 

class Task3_priv_signal(Page):
    form_model = 'player'
    form_fields = ['Guess_of_theta_signal', 'Guess_of_sigma_signal']
    def vars_for_template(player):
            ############################################################
            # Below, we store predetermined color parameters in the 
            # following code. Parameters are round_number and iq_ranking
            # dependent. We can change them anytime.
            ############################################################
            ### Round 1 ###
             if player.round_number == 1:
              if player.participant.vars['ranking']== 1:
                  color = 'green'
              elif player.participant.vars['ranking']== 2:
                  color = 'green'
              elif player.participant.vars['ranking']== 3:
                  color = 'red'
              elif player.participant.vars['ranking']== 4:
                  color = 'red'
              else:
                  color = None
            ### Round 2 ###
             elif player.round_number == 2:
              if player.participant.vars['ranking']== 1:
                  color = 'green'
              elif player.participant.vars['ranking']== 3:
                  color = 'green'
              elif player.participant.vars['ranking']== 2:
                  color = 'red'
              elif player.participant.vars['ranking']== 4:
                  color = 'red'
              else:
                  color = None
            ### Round 3 ###
             else:
              if player.participant.vars['ranking']== 2:
                  color = 'green'
              elif player.participant.vars['ranking']== 4:
                  color = 'green'
              elif player.participant.vars['ranking']== 1:
                  color = 'red'
              elif player.participant.vars['ranking']== 3:
                  color = 'red'
              else:
                  color = None
            ############################################################
            # Below, we store predetermined sigma parameters in the 
            # following code. Parameters are round_number and player_id
            # dependent. We can change them anytime.
            ############################################################
            ### Round 1 ###
             if player.round_number == 1:
              if player.id_in_group== 1:
                  sigma_signal = 1
              elif player.id_in_group== 2:
                  sigma_signal = 1
              elif player.id_in_group== 3:
                  sigma_signal = 2
              elif player.id_in_group== 4:
                  sigma_signal = 2
              else:
                  sigma_signal = None
            ### Round 2 ###
             elif player.round_number == 2:
              if player.id_in_group== 1:
                  sigma_signal = 3
              elif player.id_in_group== 2:
                  sigma_signal = 3
              elif player.id_in_group== 3:
                  sigma_signal = 4
              elif player.id_in_group== 4:
                  sigma_signal = 4
              else:
                  sigma_signal = None
            ### Round 3 ###
             else:
              if player.id_in_group== 1:
                  sigma_signal = 5
              elif player.id_in_group== 2:
                  sigma_signal = 5
              elif player.id_in_group== 3:
                  sigma_signal = 6
              elif player.id_in_group== 4:
                  sigma_signal = 6
              else:
                  sigma_signal = None

             return {
                'ranking':player.participant.vars['ranking'],
                'color': color,
                'sigma_signal':sigma_signal,
           }
 


page_sequence = [Task2, Task3_color, Task3_priv_signal]
