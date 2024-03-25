from otree.api import *
import math
import random
import csv

class C(BaseConstants):
    NAME_IN_URL = 'motivated_ambiguity'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 22


class Subsession(BaseSubsession):
    # store config parameters
    cfg_total_rounds = models.IntegerField()
    cfg_total_practice = models.IntegerField()
    cfg_round_number = models.IntegerField()
    cfg_is_practice = models.StringField()
    # cfg_parameters = models.StringField()
    cfg_is_motivated = models.StringField()
    cfg_num_signals = models.IntegerField()
    cfg_true_state = models.StringField()
    cfg_true_theta = models.FloatField()
    cfg_sigma_s2 = models.StringField()
    cfg_signals_rank1 = models.StringField()
    cfg_signals_rank2 = models.StringField()
    cfg_signals_rank3 = models.StringField()
    cfg_signals_rank4 = models.StringField()
    cfg_signals_rank5 = models.StringField()
    cfg_signals_rank6 = models.StringField()
    cfg_signals_rank7 = models.StringField()
    cfg_signals_rank8 = models.StringField()

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
    Guess_of_theta_color = models.StringField(
        label='''
        Question 1: Please make a guess of the true value of the asset in this round.
        ''')
    Guess_of_theta_signal1 = models.StringField(
        label='''
        Question 1: Please make a guess of the true value of the asset in this round.
        ''')
    Guess_of_sigma_signal1 = models.StringField(
        label='''
        Question 2: Please make a guess of the accuracy of your private signal in this round. （A value between 0.25 and 4)
        '''
    )
    Guess_of_theta_signal2 = models.StringField(
        label='''
        Question 1: Please make a guess of the true value of the asset in this round.
        ''')
    Guess_of_sigma_signal2 = models.StringField(
        label='''
        Question 2: Please make a guess of the accuracy of your private signal in this round. （A value between 0.25 and 4)
        '''
    )
    Payoff_task2 = models.IntegerField()
    Payoff_color_theta = models.IntegerField()
    Payoff_signal1_theta = models.IntegerField()
    Payoff_signal1_sigma = models.IntegerField()
    Payoff_signal2_theta = models.IntegerField()
    Payoff_signal2_sigma = models.IntegerField()
    
    grouping = models.StringField()
    marking = models.StringField()
    final_payoff = models.CurrencyField()
    iq_ranking = models.IntegerField()


    # Below are test questions:
    Test_question1 = models.StringField(
        choices=['[-5,+5]','[-6,+6]','[-7,+7]','[-8,+8]','[-9,+9]','[-10,+10]'],
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

    # import configs files
def parse_config(config_file):
    with open('motivated_ambiguity/configs/' + config_file) as f:
        rows = list(csv.DictReader(f))

    rounds = []
    for row in rows:
        rounds.append({
            'round_number': int(row['round_number']),
            'is_practice': str(row['is_practice']),
            #'parameters': str(row['parameters']),
            'is_motivated': str(row['is_motivated']),
            'num_signals': int(row['num_signals']),
            'true_state': str(row['true_state']),
            'true_theta': float(row['true_theta']),
            'sigma_s2': str(row['sigma_s2']),
            'signals_rank1': str(row['signals_rank1']),
            'signals_rank2': str(row['signals_rank2']),
            'signals_rank3': str(row['signals_rank3']),
            'signals_rank4': str(row['signals_rank4']),
            'signals_rank5': str(row['signals_rank5']),
            'signals_rank6': str(row['signals_rank6']),
            'signals_rank7': str(row['signals_rank7']),
            'signals_rank8': str(row['signals_rank8'])
        })
    return rounds
# FUNCTIONS
# PAGES

class Task2_Instructions(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1
    
    def vars_for_template(self):
        
        # img_sig_url = '/static/Motivated_Beliefs/signal.PNG'
        img_url1 = '/static/task2_example1.jpg'
        img_url2 = '/static/task2_example2.jpg'

        return {
                'img_url1': img_url1,
                'img_url2': img_url2,
            }

class Task2(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1
    form_model = 'player'
    form_fields = ['Ambiguity_attitude_elicit1','Ambiguity_attitude_elicit2','Ambiguity_attitude_elicit3',     'Ambiguity_attitude_elicit4','Ambiguity_attitude_elicit5','Ambiguity_attitude_elicit6','Ambiguity_attitude_elicit7','Ambiguity_attitude_elicit8','Ambiguity_attitude_elicit9','Ambiguity_attitude_elicit10']

class Task3_Instructions_basicmath(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1
    
    def vars_for_template(self):
        std_normal_distribution = '/static/stdnormaldist.png'

        return {
                'std_normal_distribution': std_normal_distribution,
            }
           
class Task3_Instructions_maintask(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1
    
    def vars_for_template(self):
        std_normal_distribution = '/static/stdnormaldist.png'

        return {
                'std_normal_distribution': std_normal_distribution,
            }
    
class Task3_Instructions_type1info(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1

    def vars_for_template(self):
        grouping_img = '/static/grouping.png'
        return {
                'grouping_img': grouping_img,
            }
    
class Task3_Instructions_type2info(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1

class Task3_Instructions_survey1(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1
    def vars_for_template(self):
        survey1_img = '/static/survey1_img.png'
        return {
                'survey1_img': survey1_img,
            }



class Task3_Instructions_survey2(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1  
    def vars_for_template(self):
        survey2_img = '/static/survey2_img.png'
        return {
                'survey2_img': survey2_img,
            }
    
class Task3_Instructions_survey2_2(Page):
    @staticmethod
    def is_displayed(player):
       return player.round_number == 1   
    def vars_for_template(self):
        survey2_img = '/static/survey2_img.png'
        return {
                'survey2_img': survey2_img,
            }
    
class Task3_Instructions_pay_time(Page):
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
        
class WaitPage1(WaitPage):
    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        # get players ranking from the IQ test
        for p in subsession.get_players():
            p.iq_ranking = p.participant.vars['ranking']

        # # randomly group players into 2
        # subsession.group_randomly(fixed_id_in_group=True)

        # group assignment based on iq ranking
        players = subsession.get_players()
        player_values = [(p.id_in_subsession, p.iq_ranking) for p in players]
        sorted_players = sorted(player_values, key=lambda x: x[1], reverse=False)
        seed = 10000 + subsession.round_number*100
        random.seed(seed)
        random.shuffle(sorted_players)
        #print(sorted_players)
        matrix = []
        player_list = [p for p, _ in sorted_players]
        for i in range(0, len(players), C.PLAYERS_PER_GROUP):
            matrix.append(player_list[i: i + C.PLAYERS_PER_GROUP])
        #print('matrix is', matrix)
        subsession.set_group_matrix(matrix)

        # import configs file and calculate round numbers
        config = parse_config(subsession.session.config['config_file'])
        subsession.cfg_total_rounds = len(config)
        subsession.cfg_total_practice = sum([1 for row in config if row.get('is_practice', '').upper() == 'TRUE'])
        if subsession.round_number > subsession.cfg_total_rounds:
            return

        # import parameters of the current round
        parameters = config[subsession.round_number - 1]
        subsession.cfg_round_number = parameters['round_number']
        subsession.cfg_is_practice = parameters['is_practice']
        #subsession.cfg_parameters = parameters['parameters']
        subsession.cfg_is_motivated = parameters['is_motivated']
        subsession.cfg_num_signals = parameters['num_signals']
        subsession.cfg_true_state = parameters['true_state']
        subsession.cfg_true_theta = parameters['true_theta']
        subsession.cfg_sigma_s2 = parameters['sigma_s2']
        subsession.cfg_signals_rank1 = parameters['signals_rank1']
        subsession.cfg_signals_rank2 = parameters['signals_rank2']
        subsession.cfg_signals_rank3 = parameters['signals_rank3']
        subsession.cfg_signals_rank4 = parameters['signals_rank4']
        subsession.cfg_signals_rank5 = parameters['signals_rank5']
        subsession.cfg_signals_rank6 = parameters['signals_rank6']
        subsession.cfg_signals_rank7 = parameters['signals_rank7']
        subsession.cfg_signals_rank8 = parameters['signals_rank8']


        # group assignment for each grouping
        for g in subsession.get_groups():
            # get the two players in a group
            p1 = g.get_player_by_id(1)
            p2 = g.get_player_by_id(2)
            # without motivated belief
            if subsession.cfg_is_motivated == 'FALSE':
                p1.grouping = random.choice(['H', 'L'])
                if p1.grouping == 'H':
                    p2.grouping = 'L'
                else:
                    p2.grouping = 'H'
            # with motivated belief
            else:
                if p1.participant.vars['ranking'] < p2.participant.vars['ranking']:
                    p1.grouping = 'H'
                    p2.grouping = 'L'
                else:
                    p1.grouping = 'L'
                    p2.grouping = 'H'

        # player assignment for each player
        for p in subsession.get_players():
            if subsession.cfg_true_state == 'B':
                if p.grouping == 'H':
                    p.marking = 'red'
                else:
                    p.marking = 'green'
            else:
                if p.grouping == 'H':
                    p.marking = 'green'
                else:
                    p.marking = 'red'



class Task3_color(Page):
        form_model = 'player'
        form_fields = ['Guess_of_theta_color']
        def vars_for_template(player):
             return {
 #               'Ambiguity_attitude_elicit1': player.Ambiguity_attitude_elicit1,
                'ranking':player.participant.vars['ranking'],
                'color': player.marking,
                'round_number':player.round_number,
   #             'colorgreen':colorgreen,
           }
 

class Task3_priv_signal1(Page):
    form_model = 'player'
    form_fields = ['Guess_of_theta_signal1', 'Guess_of_sigma_signal1']
    def vars_for_template(player):
        # Save players' signals by ranking. One by one:
        r1_signals_string = player.subsession.cfg_signals_rank1.split()
        r1_signals = [float(signal) for signal in r1_signals_string]

        r2_signals_string = player.subsession.cfg_signals_rank2.split()
        r2_signals = [float(signal) for signal in r2_signals_string]

        r3_signals_string = player.subsession.cfg_signals_rank3.split()
        r3_signals = [float(signal) for signal in r3_signals_string]

        r4_signals_string = player.subsession.cfg_signals_rank4.split()
        r4_signals = [float(signal) for signal in r4_signals_string]

        r5_signals_string = player.subsession.cfg_signals_rank5.split()
        r5_signals = [float(signal) for signal in r5_signals_string]

        r6_signals_string = player.subsession.cfg_signals_rank6.split()
        r6_signals = [float(signal) for signal in r6_signals_string]

        r7_signals_string = player.subsession.cfg_signals_rank7.split()
        r7_signals = [float(signal) for signal in r7_signals_string]

        r8_signals_string = player.subsession.cfg_signals_rank8.split()
        r8_signals = [float(signal) for signal in r8_signals_string]
        return {
                'ranking':player.participant.vars['ranking'],
                'color': player.marking,
                'r1_sigma_signal1':r1_signals[0],
                'r1_sigma_signal2':r1_signals[1],
                'r2_sigma_signal1':r2_signals[0],
                'r2_sigma_signal2':r2_signals[1],
                'r3_sigma_signal1':r3_signals[0],
                'r3_sigma_signal2':r3_signals[1],
                'r4_sigma_signal1':r4_signals[0],
                'r4_sigma_signal2':r4_signals[1],
                'r5_sigma_signal1':r5_signals[0],
                'r5_sigma_signal2':r5_signals[1],
                'r6_sigma_signal1':r6_signals[0],
                'r6_sigma_signal2':r6_signals[1],
                'r7_sigma_signal1':r7_signals[0],
                'r7_sigma_signal2':r7_signals[1],
                'r8_sigma_signal1':r8_signals[0],
                'r8_sigma_signal2':r8_signals[1],
                'round_number':player.round_number,
           }
 
class Task3_priv_signal2(Page):
        @staticmethod
        def is_displayed(player):
          if player.subsession.cfg_num_signals == 2:
             return True
          else:
             return False
        form_model = 'player'
        form_fields = ['Guess_of_theta_signal2', 'Guess_of_sigma_signal2']
        def vars_for_template(player):
            # Save players' signals by ranking. One by one:
            r1_signals_string = player.subsession.cfg_signals_rank1.split()
            r1_signals = [float(signal) for signal in r1_signals_string]

            r2_signals_string = player.subsession.cfg_signals_rank2.split()
            r2_signals = [float(signal) for signal in r2_signals_string]

            r3_signals_string = player.subsession.cfg_signals_rank3.split()
            r3_signals = [float(signal) for signal in r3_signals_string]

            r4_signals_string = player.subsession.cfg_signals_rank4.split()
            r4_signals = [float(signal) for signal in r4_signals_string]

            r5_signals_string = player.subsession.cfg_signals_rank5.split()
            r5_signals = [float(signal) for signal in r5_signals_string]

            r6_signals_string = player.subsession.cfg_signals_rank6.split()
            r6_signals = [float(signal) for signal in r6_signals_string]

            r7_signals_string = player.subsession.cfg_signals_rank7.split()
            r7_signals = [float(signal) for signal in r7_signals_string]

            r8_signals_string = player.subsession.cfg_signals_rank8.split()
            r8_signals = [float(signal) for signal in r8_signals_string]

            return {
                'ranking':player.participant.vars['ranking'],
                'color': player.marking,
                'r1_sigma_signal1':r1_signals[0],
                'r1_sigma_signal2':r1_signals[1],
                'r2_sigma_signal1':r2_signals[0],
                'r2_sigma_signal2':r2_signals[1],
                'r3_sigma_signal1':r3_signals[0],
                'r3_sigma_signal2':r3_signals[1],
                'r4_sigma_signal1':r4_signals[0],
                'r4_sigma_signal2':r4_signals[1],
                'r5_sigma_signal1':r5_signals[0],
                'r5_sigma_signal2':r5_signals[1],
                'r6_sigma_signal1':r6_signals[0],
                'r6_sigma_signal2':r6_signals[1],
                'r7_sigma_signal1':r7_signals[0],
                'r7_sigma_signal2':r7_signals[1],
                'r8_sigma_signal1':r8_signals[0],
                'r8_sigma_signal2':r8_signals[1],
                'round_number':player.round_number,
           }
class Practice_done(Page):
        @staticmethod
        def is_displayed(player):
              if player.subsession.cfg_is_practice == 'TRUE':
                 return True
              else:
                 return False
#	def before_next_page(self):
#		self.player.save()
class Payoff_page(Page):
        @staticmethod
        def is_displayed(player):
              if player.round_number == player.subsession.cfg_total_rounds:
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
              
page_sequence = [Task2_Instructions, Task2, 
                 Task3_Instructions_basicmath, Task3_Instructions_maintask, Task3_Instructions_type1info, Task3_Instructions_type2info, 
                 Task3_Instructions_survey1, Task3_Instructions_survey2, Task3_Instructions_survey2_2, Task3_Instructions_pay_time,
                 Test_questions, WaitPage1,  Task3_color, Task3_priv_signal1, Task3_priv_signal2, Practice_done, Payoff_page]

