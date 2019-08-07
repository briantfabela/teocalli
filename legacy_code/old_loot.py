'''
    def loot(self):
        '''Generate a dict of loot items based on location and player skills'''

        loot_droped = {}
        materials = ['gold', 'silver', 'jade', 'obsidian', 'turquoise']
        # add amethyst, pearls, emerald <- rarer but not necessarily more val

        for _ in range(randint(1, 3)): # generate a total inventory for loot
            self.addToInventory({choice(materials):randint(1, 3)}, loot_droped)

        # TODO: consider triggering an 'Event' instance with its unique events

        ### THIS AREA WILL BE REPLACES BY EVENTS ###

        # aquire xp
        xp_drop = randint(1, 5)
        # TODO: make the probability dependant on a player skill
        if random() > 0.85 :
            xp_drop += randint(5, 10)

        self.current_site.xp_earned += xp_drop
        self.xp += xp_drop

        # loose some hp; based on risk
        hp_loss = 0
        if random() * 100 <= self.current_site.risk:
            max_dmg = 2 + self.current_site.risk //  10 # 2 - risk // 10
            hp_loss += round(randint(1, max_dmg) * 
                       (1 + self.current_site.risk / 100))
            self.hp -= hp_loss

        # increase site risk
        risk_gain = 0
        if random() < 0.6: # consider skill that reduces likelyhood of increase
            risk_gain += randint(1, 3) # cosnider skill that mitigates max gain
            self.current_site.risk += risk_gain

        ### THIS AREA WILL BE REPLACES BY EVENTS ###

        # generate a chance to aquire the site's legendary loot
        if not self.current_site.legend_art_collect: # if not yet collected
            if random() >= 0.95: # make a player's skill affect this prob
                # print artifact discovery event to console
                print(f"You found {self.current_site.legend_artif.name_full}!")
                print(f"This is a *{self.current_site.legend_artif.rarity}* "\
                       "item")
                self.addToInventory({self.current_site.legend_artif.name : 1},
                                    loot_droped)
                self.current_site.legend_art_collect = True

        # add all collected loot thus far to self.current_site.site_loot
        self.addToInventory(loot_droped, self.current_site.site_loot)

        self.loot_print(risk_gain, hp_loss, xp_drop, loot_droped)

    # TODO: Consider adding medkits, torches, antidotes, and ropes to the game

    def loot_print(self, risk_gain, hp_loss, xp_drop, loot_droped):
        '''Print self.loot() events to console'''
        event_str = '' # stores the string to be printed. For concatenation.

        # 1st Line: Risk Gain and/or HP Loss and XP gain
        if hp_loss and risk_gain:
            event_str += f"+{risk_gain}% risk, -{hp_loss} HP"
        elif risk_gain:
            event_str += f"+{risk_gain}% risk" # xp gain
        elif hp_loss:
            event_str += f"-{hp_loss} HP" # hp loss

        if len(event_str): event_str+=", " # if the string has no xp or hp stats
        event_str += f"+{xp_drop} XP\n" # add xp gain

        # 2nd Line: Total Risk & total HP loss
        event_str += f"Total Risk: {self.current_site.risk}%, HP: {self.hp}, "\
                     f"Site XP: {self.current_site.xp_earned}\n"

        # rest of string's lines: Loot dropped
        event_str += "Loot:\n"
        for item, amount in loot_droped.items():
            event_str += f"\t{item}: {amount}\n"

        # end function
        print(event_str)
'''