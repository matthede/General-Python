class nba:
    
    import random
    
    Bucks = {'Name': 'Bucks',
             'FG': 47.6,
             '3pFG': 35.5,
             'FT': 74.2,
             'OREB': 9.5,
             'DREB': 42.2,
             'TOV': 15.1,
             'FTP': 74.2,
             'FPP': 20.7}
    
    Raptors = {'Name': 'Raptors',
             'FG': 45.8,
             '3pFG': 37.4,
             'FT': 79.6,
             'OREB': 9.5,
             'DREB': 35.9,
             'TOV': 14.8,
             'FTP': 79.9,
             'FPP': 18.1,
             }
    
    posessions = 200
    
    def __init__(self):
        pass
        
    def nba_game(self, team1, team2):
        print("Welcome to the NBA")
        print("Tonight's match up is " + team1['Name'] + ' vs. ' + team2['Name'])
        
        posession = self.posessions
        tipoff = random.randint(0, 100)
        if tipoff > 50:
            arrow = 'team1'
        else:
            arrow = 'team2'
            
        team1_score = 0
        team2_score = 0
        
        while posession > 0:
            if arrow == 'team1':
                posession -=1
                if random.uniform(0, 100) < team1['FG']:
                    team1_score += 2
                    arrow = 'team2'
                else:
                    arrow = 'team2'
            else:
                posession -= 1
                if random.uniform(0, 100) < team1['FG']:
                    team2_score += 2
                    arrow = 'team1'
                else:
                    arrow = 'team1'
                    
        def overtime(team1, team2, fg1, fg2, name1, name2):
            posession = 30
            
            team1_name = name1
            team2_name = name2
            team1_score = team1
            team2_score = team2
            team1_fg = fg1
            team2_fg = fg2
            
            tipoff = random.uniform(0, 100)
    
            if tipoff > 50:
                arrow = 'team1'
            else:
                arrow = 'team2'
    
            while posession > 0:
                if arrow == 'team1':
                    posession -=1
                    if random.uniform(0, 100) < team1_fg:
                        team1_score += 2
                        arrow = 'team2'
                    else:
                        arrow = 'team2'
                else:
                    posession -= 1
                    if random.uniform(0, 100) < team2_fg:
                        team2_score += 2
                        arrow = 'team1'
                    else:
                        arrow = 'team1'
    
            if (posession == 0) and (team1_score == team2_score):
                overtime(team1_score, team2_score, team1_fg, team2_fg, team1_name, team2_name)
            else:
                print('Game over.')
                print('Final Score in Overtime.')
                print('{}: {}'.format(team1_name, str(team1_score)))
                print('{}: {}'.format(team2_name, str(team2_score)))
                
                
            
        if (posession == 0) and (team1_score == team2_score):
            overtime(team1_score, team2_score, team1['FG'], team2['FG'], team1['Name'], team2['Name'])
            return
        else:
            print('Game over.')
            print('Final Score')
            print('{}: {}'.format(team1['Name'], str(team1_score)))
            print('{}: {}'.format(team2['Name'], str(team2_score)))
                
        
if __name__ == '__main__':
    game = nba()

    game.nba_game(game.Bucks, game.Raptors)
