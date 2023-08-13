
#[derive(Debug, PartialEq, Eq)]
pub enum TaskState {
    ToDo,
    Done,
}

#[derive(Debug)]
pub struct Task {
    title: String,
    state: TaskState,
}

impl Task {
    pub fn new(title: &str) -> Self {
        Self {
            title: String::from(title),
            state: TaskState::ToDo,
        }
    }

    pub fn switch_state(&mut self) {
        self.state = match self.state {
            TaskState::ToDo => TaskState::Done,
            TaskState::Done => TaskState::ToDo,
        }
    }

    pub fn title(&self) -> &str {
        &self.title
    }

    pub fn is_done(&self) -> bool {
        self.state == TaskState::Done
    }
}
