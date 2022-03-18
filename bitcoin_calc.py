#Need year when last bitcoin will be mined
#When will 98% of bitcoins be mined

#'We know there is 21m Bitcoins'
#'Block reward halves every 210k blocks'
#'block mined every 10mins'
#'initial block reward = 50BTC'

#(Issue block reward + 10mins) every block until block halving period
#half block reward
#repeat until x = 98% of 21000000


max_supply = 21000000 #bitcoins
time_per_block = 10 #minutes
halving_multiplier = 0.5
block_reward = 50 #bitcoins
halving_time = 210000 #blocks
blocks_mined = 0
btc_mined = 0
time = 0

def counter(time, btc_mined):
    time = time + 10
    btc_mined = btc_mined + 1

def how_many_blocks(percent_mined):
    percentage = percent_mined/100
    block_we_are_looking_for = percentage*max_supply

    block_number = 0

    while (block_number <= block_we_are_looking_for):
        block_number = block_number+1

def time_to_mine_x(percent_mined):
    percentage = percent_mined/100
    block_we_are_looking_for = percentage*max_supply

    while (btc_mined <= ((percent_mined/100)*max_supply)):

        if (blocks_mined <= halving_time):
            blocks_mined = blocks_mined + 1
            btc_mined = btc_mined + block_reward
            time = time + 10
        else:
            block_reward = block_reward * halving_multiplier
            blocks_mined = 0
    print(time)
