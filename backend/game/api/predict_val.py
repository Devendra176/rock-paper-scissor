import logging
logging.basicConfig(filename='score.log' ,level=logging.INFO,format='%(asctime)s : %(levelname)s : %(message)s')

ROCK = 1
PAPER = 2
SCISSOR = 3

options = {1:'ROCK', 2:'PAPER', 3:'SCISSOR'}

class PredictValueMethod():
    def __init__(self, user_val, predicted_val):
        self.user_val = user_val
        self.predicted_val = predicted_val


    def write_log(self):
        pass

    def find_score(self):
        user_val = self.user_val
        predicted_val = self.predicted_val
        response = {}
        response['user_data'] = self.user_val
        response['com_value'] = options[self.predicted_val]
        response['com_data'] = self.predicted_val

        if user_val == predicted_val:
            response['msg'] = 'this round is Tie Both choose {}'.format(options[user_val])
            response['user_score'] = False
            response['com_score'] = False
            logging.info('user Selected {}'.format(options[user_val]))
            logging.info('computer Selected {}'.format(options[predicted_val]))
            logging.info(response['msg'])

        elif user_val == ROCK and predicted_val == PAPER:
            response['msg'] = 'you loose, computer choose Paper.'
            response['user_score'] = False
            response['com_score'] = True
            logging.info('user Selected {}'.format(options[user_val]))
            logging.info('computer Selected {}'.format(options[predicted_val]))
            logging.info(response['msg'])

        elif user_val == ROCK and predicted_val == SCISSOR:
            response['msg'] = 'you win,computer select scissor'
            response['user_score'] = True
            response['com_score'] = False
            logging.info('user Selected {}'.format(options[user_val]))
            logging.info('computer Selected {}'.format(options[predicted_val]))
            logging.info(response['msg'])

        elif user_val == PAPER and predicted_val == SCISSOR:
            response['msg'] = 'you loose,computer select scissor'
            response['user_score'] = False
            response['com_score'] = True
            logging.info('user Selected {}'.format(options[user_val]))
            logging.info('computer Selected {}'.format(options[predicted_val]))

        elif user_val == PAPER and predicted_val == ROCK:
            response['msg'] = 'you win,computer select rock'
            response['user_score'] = True
            response['com_score'] = False
            logging.info('user Selected {}'.format(options[user_val]))
            logging.info('computer Selected {}'.format(options[predicted_val]))
            logging.info(response['msg'])

        elif user_val == SCISSOR and predicted_val == ROCK:
            response['msg'] = 'you loose,computer select rock'
            response['user_score'] = False
            response['com_score'] = True
            logging.info('user Selected {}'.format(options[user_val]))
            logging.info('computer Selected {}'.format(options[predicted_val]))
            logging.info(response['msg'])

        elif user_val == SCISSOR and predicted_val == PAPER:
            response['msg'] = 'you win ,computer select paper'
            response['user_score'] = True
            response['com_score'] = False
            logging.info('user Selected {}'.format(options[user_val]))
            logging.info('computer Selected {}'.format(options[predicted_val]))
            logging.info(response['msg'])

        else:
            response['msg'] = 'invalid: choose any one -- rock, paper, scissors'
            response['user_score'] = False
            response['com_score'] = False
            logging.info(response['msg'])
        return response
    
    def final_result(self):
        response = {}
        if self.user_val > self.predicted_val:
            response['msg'] = 'User won the game! click at New game To play again'
            response['user_won'] = True
            logging.info('User Won the game! score: user-{}, computer-{}'.format(self.user_val, self.predicted_val))
        elif self.user_val == self.predicted_val:
            response['msg'] = 'This game is tie! click at New game To play again'
            response['user_won'] = None
            logging.info('This is Tie score: user-{}, computer-{}'.format(self.user_val,self.predicted_val))
        else:
            response['msg'] = 'Computer won the game! click at New game To play again'
            response['user_won'] = False
            logging.info('computer won the game score: user-{}, computer-{}'.format(self.predicted_val,self.user_val))
        return response
