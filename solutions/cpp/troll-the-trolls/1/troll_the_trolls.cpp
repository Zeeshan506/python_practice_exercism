namespace hellmath {

// TODO: Task 1 - Define an `AccountStatus` enumeration to represent the four
// account types: `troll`, `guest`, `user`, and `mod`.
    enum class AccountStatus {
    mod,
    user,
    guest,
    troll
    };

// TODO: Task 1 - Define an `Action` enumeration to represent the three
// permission types: `read`, `write`, and `remove`.
    enum class Action{
    read,
    write,
    remove
    };
    
// TODO: Task 2 - Implement the `display_post` function, that gets two arguments
// of `AccountStatus` and returns a `bool`. The first argument is the status of
// the poster, the second one is the status of the viewer.
    bool display_post(AccountStatus s_o_p, AccountStatus s_o_v ){
        switch(s_o_p){
            case AccountStatus::troll:
                if(s_o_v == AccountStatus::troll){
                    return true;
                } else{
                    return false;
                }
            default:
                return true;
        }
        return false;
    }

// TODO: Task 3 - Implement the `permission_check` function, that takes an
// `Action` as a first argument and an `AccountStatus` to check against. It
// should return a `bool`.
    bool permission_check(Action a, AccountStatus b){
        switch(b){
            case AccountStatus::troll:
            case AccountStatus::user:
                return(a == Action::read || a == Action::write);

            case AccountStatus::mod:
                return(a == Action::read || a == Action::write || a ==Action::remove);

            case AccountStatus::guest:
                return(a==Action::read);
        }
        return false;
    }
// TODO: Task 4 - Implement the `valid_player_combination` function that
// checks if two players can join the same game. The function has two parameters
// of type `AccountStatus` and returns a `bool`.
    bool valid_player_combination(AccountStatus a, AccountStatus b){
    switch(a){
        case AccountStatus::troll:
            return a == b;
        case AccountStatus::guest:
            return false;
        default:
            switch(b){
                case AccountStatus::troll:
                return a == b;
                case AccountStatus::guest:
                return false;
                default:
                    return true;
            }
    }
    }
// TODO: Task 5 - Implement the `has_priority` function that takes two
// `AccountStatus` arguments and returns `true`, if and only if the first
// account has a strictly higher priority than the second.
    bool has_priority(AccountStatus first, AccountStatus second){
        return(static_cast<int>(first) < static_cast<int>(second));
    }
}  // namespace hellmath
