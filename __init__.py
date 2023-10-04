from otree.api import *
import math
import random

class C(BaseConstants):
    NAME_IN_URL = 'motivated_ambiguity'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 6


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
    Guess_of_theta_color = models.IntegerField( min=1,max=100,
        label='''
        ''')
    Guess_of_theta_signal1 = models.IntegerField( min=1,max=100,
        label='''
        Guess of Theta.
        ''')
    Guess_of_sigma_signal1 = models.StringField(
        choices=['[-5,+5]','[-10,+10]','[-15,+15]','[-20,+20]','[-25,+25]','[-30,+30]'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        Guess of Sigma.
        '''
    )
    Guess_of_theta_signal2 = models.IntegerField( min=1,max=100,
        label='''
        Guess of Theta.
        ''')
    Guess_of_sigma_signal2 = models.StringField(
        choices=['[-5,+5]','[-10,+10]','[-15,+15]','[-20,+20]','[-25,+25]','[-30,+30]'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        Guess of Sigma.
        '''
    )
    Payoff_task2 = models.IntegerField()
    Payoff_color_theta = models.IntegerField()
    Payoff_signal1_theta = models.IntegerField()
    Payoff_signal1_sigma = models.IntegerField()
    Payoff_signal2_theta = models.IntegerField()
    Payoff_signal2_sigma = models.IntegerField()
    
    # Below are test questions:
    Test_question1 = models.StringField(
        choices=['[-5,+5]','[-10,+10]','[-15,+15]','[-20,+20]','[-25,+25]','[-30,+30]'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        Question 1: Which one of the following means the most precise?
        '''
    )
    Test_question2 = models.StringField(
        choices=['10%','1%','80%','0.1%','50%'],
        widget=widgets.RadioSelectHorizontal,
        label='''
        Question 2: What is the probability that the true theta takes value of 57?
        '''
    )
# FUNCTIONS
# PAGES

class Instructions(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1

        
class Test_questions(Page):
    form_model = 'player'
    form_fields = ['Test_question1', 'Test_question2']

    @staticmethod
    def is_displayed(player):
       return player.round_number == 1

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['Test_question1'] != "[-5,+5]":
            return 'Your answer to question 1 is wrong. Please answer that question again.'
        if values['Test_question2'] != "1%":
            return 'Your answer to question 2 is wrong. Please answer that question again.'
        
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
             elif player.round_number == 3:
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
            ### Round 4 ###
             elif player.round_number == 4:
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
            ### Round 5 ###
             elif player.round_number == 5:
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
            ### Round 6 ###
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
                'round_number':player.round_number,
   #             'colorgreen':colorgreen,
           }
 

class Task3_priv_signal1(Page):
    form_model = 'player'
    form_fields = ['Guess_of_theta_signal1', 'Guess_of_sigma_signal1']
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
             elif player.round_number == 3:
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
             ### Round 4 ###
             elif player.round_number == 4:
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
             ### Round 5 ###
             elif player.round_number == 5:
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
            ### Round 6 ###
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
                  sigma_signal1 = 1
              elif player.id_in_group== 2:
                  sigma_signal1 = 1
              elif player.id_in_group== 3:
                  sigma_signal1 = 7
              elif player.id_in_group== 4:
                  sigma_signal1 = 7
              else:
                  sigma_signal1 = None
            ### Round 2 ###
             elif player.round_number == 2:
              if player.id_in_group== 1:
                  sigma_signal1 = 3
              elif player.id_in_group== 2:
                  sigma_signal1 = 3
              elif player.id_in_group== 3:
                  sigma_signal1 = 4
              elif player.id_in_group== 4:
                  sigma_signal1 = 4
              else:
                  sigma_signal1 = None
            ### Round 3 ###
             elif player.round_number == 3:
              if player.id_in_group== 1:
                  sigma_signal1 = 3
              elif player.id_in_group== 2:
                  sigma_signal1 = 3
              elif player.id_in_group== 3:
                  sigma_signal1 = 4
              elif player.id_in_group== 4:
                  sigma_signal1 = 4
              else:
                  sigma_signal1 = None
            ### Round 4 ###
             elif player.round_number == 4:
              if player.id_in_group== 1:
                  sigma_signal1 = 3
              elif player.id_in_group== 2:
                  sigma_signal1 = 3
              elif player.id_in_group== 3:
                  sigma_signal1 = 4
              elif player.id_in_group== 4:
                  sigma_signal1 = 4
              else:
                  sigma_signal1 = None
            ### Round 5 ###
             elif player.round_number == 5:
              if player.id_in_group== 1:
                  sigma_signal1 = 3
              elif player.id_in_group== 2:
                  sigma_signal1 = 3
              elif player.id_in_group== 3:
                  sigma_signal1 = 4
              elif player.id_in_group== 4:
                  sigma_signal1 = 4
              else:
                  sigma_signal1 = None
            ### Round 6 ###
             else:
              if player.id_in_group== 1:
                  sigma_signal1 = 5
              elif player.id_in_group== 2:
                  sigma_signal1 = 5
              elif player.id_in_group== 3:
                  sigma_signal1 = 8
              elif player.id_in_group== 4:
                  sigma_signal1 = 8
              else:
                  sigma_signal1 = None

             return {
                'ranking':player.participant.vars['ranking'],
                'color': color,
                'sigma_signal1':sigma_signal1,
                'round_number':player.round_number,
           }
 
class Task3_priv_signal2(Page):
        @staticmethod
        def is_displayed(player):
          if player.round_number == 1:
             return True
          elif player.round_number == 3:
              return True
          elif player.round_number == 4:
              return True
          else:
             return False
        form_model = 'player'
        form_fields = ['Guess_of_theta_signal2', 'Guess_of_sigma_signal2']
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
             elif player.round_number == 3:
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
             ### Round 4 ###
             elif player.round_number == 4:
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
             ### Round 5 ###
             elif player.round_number == 5:
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
            ### Round 6 ###
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
                  sigma_signal2 = 200
              elif player.id_in_group== 2:
                  sigma_signal2 = 200
              elif player.id_in_group== 3:
                  sigma_signal2 = 200
              elif player.id_in_group== 4:
                  sigma_signal2 = 200
              else:
                  sigma_signal2 = None
            ### Round 2 ###
             elif player.round_number == 2:
              if player.id_in_group== 1:
                  sigma_signal2 = 200
              elif player.id_in_group== 2:
                  sigma_signal2 = 200
              elif player.id_in_group== 3:
                  sigma_signal2 = 200
              elif player.id_in_group== 4:
                  sigma_signal2 = 200
              else:
                  sigma_signal2 = None
            ### Round 3 ###
             elif player.round_number == 3:
              if player.id_in_group== 1:
                  sigma_signal2 = 200
              elif player.id_in_group== 2:
                  sigma_signal2 = 200
              elif player.id_in_group== 3:
                  sigma_signal2 = 200
              elif player.id_in_group== 4:
                  sigma_signal2 = 200
              else:
                  sigma_signal2 = None
            ### Round 4 ###
             elif player.round_number == 4:
              if player.id_in_group== 1:
                  sigma_signal2 = 200
              elif player.id_in_group== 2:
                  sigma_signal2 = 200
              elif player.id_in_group== 3:
                  sigma_signal2 = 200
              elif player.id_in_group== 4:
                  sigma_signal2 = 200
              else:
                  sigma_signal2 = None
            ### Round 5 ###
             elif player.round_number == 5:
              if player.id_in_group== 1:
                  sigma_signal2 = 200
              elif player.id_in_group== 2:
                  sigma_signal2 = 200
              elif player.id_in_group== 3:
                  sigma_signal2 = 200
              elif player.id_in_group== 4:
                  sigma_signal2 = 200
              else:
                  sigma_signal2 = None
            ### Round 6 ###
             else:
              if player.id_in_group== 1:
                  sigma_signal2 = 200
              elif player.id_in_group== 2:
                  sigma_signal2 = 200
              elif player.id_in_group== 3:
                  sigma_signal2 = 200
              elif player.id_in_group== 4:
                  sigma_signal2 = 200
              else:
                  sigma_signal2 = None

             return {
                'ranking':player.participant.vars['ranking'],
                'color': color,
                'sigma_signal2':sigma_signal2,
                'round_number':player.round_number,
           }
class Practice_done(Page):
        @staticmethod
        def is_displayed(player):
              if player.round_number == 2:
                 return True
              else:
                 return False
#	def before_next_page(self):
#		self.player.save()
class Payoff_page(Page):
        @staticmethod
        def is_displayed(player):
              if player.round_number == 6:
                 return True
              else:
                 return False
              
        def vars_for_template(player):
                # The true values of theta are stored in the following list:
                true_theta_list = [10,20,30,40,50,60]
              
                # The following code privdes a random round to determine our payoffs:
                list_rounds = [3, 4, 5, 6]
                Random_picked_round = random.choice(list_rounds)
                # "Random_round_player" tells the followup codes which randomly picked round should we access 
                # player's elicited beliefs.
                Random_round_player = player.in_round(Random_picked_round)
                ###############################################################
                ###############################################################
                ###############################################################
                ############### Payoff in Experimental Points #################
                ###############################################################
                ###############################################################
                ###############################################################
                # The following code calculates our payoff (in Experimental points) of the randomly selected round.
                # Please note that "payoff_theta_signal2" is only available in rounds with two private signals.
                if Random_picked_round == 3:
                    # Below, we calculate each of the payoff earned by answering each question in that randomly picked round.
                    payoff_theta_color = (int) (100 - (math.pow((Random_round_player.Guess_of_theta_color - true_theta_list[Random_picked_round-1]),2)))
                    payoff_theta_signal1 = (int) (100 - (math.pow((Random_round_player.Guess_of_theta_signal1 - true_theta_list[Random_picked_round-1]),2)))
                    payoff_theta_signal2 = (int) (100 - (math.pow((Random_round_player.Guess_of_theta_signal2 - true_theta_list[Random_picked_round-1]),2)))
                    # Below, we add up all the payoffs of that randomly picked round for our final payoff.
                    payoff_of_random_round = payoff_theta_color + payoff_theta_signal1 + payoff_theta_signal2
                elif Random_picked_round == 4:
                    # Below, we calculate each of the payoff earned by answering each question in that randomly picked round.
                    payoff_theta_color = (int) (100 - (math.pow((Random_round_player.Guess_of_theta_color - true_theta_list[Random_picked_round-1]),2)))
                    payoff_theta_signal1 = (int) (100 - (math.pow((Random_round_player.Guess_of_theta_signal1 - true_theta_list[Random_picked_round-1]),2)))
                    payoff_theta_signal2 = (int) (100 - (math.pow((Random_round_player.Guess_of_theta_signal2 - true_theta_list[Random_picked_round-1]),2)))
                    # Below, we add up all the payoffs of that randomly picked round for our final payoff.
                    payoff_of_random_round = payoff_theta_color + payoff_theta_signal1 + payoff_theta_signal2
                else:
                    # Below, we calculate each of the payoff earned by answering each question in that randomly picked round.
                    payoff_theta_color = (int) (100 - (math.pow((Random_round_player.Guess_of_theta_color - true_theta_list[Random_picked_round-1]),2)))
                    payoff_theta_signal1 = (int) (100 - (math.pow((Random_round_player.Guess_of_theta_signal1 - true_theta_list[Random_picked_round-1]),2)))
                    # Below, we add up all the payoffs of that randomly picked round for our final payoff. 
                    payoff_of_random_round = payoff_theta_color + payoff_theta_signal1
                ###############################################################
                ###############################################################
                ###############################################################
                ############### Payoff in Real World Currency #################
                ###############################################################
                ###############################################################
                ###############################################################
                conversion_rate = .002
                participation_fee = 7
                IQ_test_payoff = 5
                player.payoff = math.ceil(payoff_of_random_round*conversion_rate + participation_fee + IQ_test_payoff)
                ###############################################################
                ###############################################################
                ###############################################################
                return {
                   'true_theta_random_picked_round': true_theta_list[Random_picked_round-1],
                   'random_picked_round': Random_picked_round,
                   'payoff': payoff_of_random_round,
                }
              
page_sequence = [Instructions, Test_questions, Task2, Task3_color, Task3_priv_signal1, Task3_priv_signal2, Practice_done, Payoff_page]

