use cursive::views::{Dialog, NamedView, ViewRef, LinearLayout, SelectView};
use cursive::view::{View, CannotFocus};
use cursive::event::{Event, EventResult, MouseEvent};
use cursive::direction;
use todo_tui::Task;


fn main() {
    let mut siv = cursive::crossterm();

    siv.add_layer(
        Dialog::default()
            .title("To Do")
            .button("Add task", |siv| {
                let mut list: ViewRef<LinearLayout> = siv.find_name("list").unwrap();
                list.add_child(TaskView::new("Test"));
            })
            .content(NamedView::new("list", LinearLayout::vertical()))
    );

    siv.run();
}

struct TaskView {
    task: Task,
}

impl TaskView {
    fn new(title: &str) -> Self {
        Self {
            task: Task::new(title),
        }
    }
}

impl View for TaskView {
    fn draw(&self, printer: &cursive::Printer) {
        let mut text = String::from(if self.task.is_done() { "[x] " } else { "[ ] " });
        text.push_str(self.task.title());

        printer.print((0, 0), &text);
    }

    fn on_event(&mut self, event: Event) -> EventResult {
        match event {
            Event::Mouse { offset:  _, position: _, event: MouseEvent::Release(_) } => {
                self.task.switch_state();
                return EventResult::Consumed(None);
            },
            _ => {}
        }

        EventResult::Ignored
    }

    fn take_focus(
            &mut self,
            _source: direction::Direction,
        ) -> Result<EventResult, CannotFocus> {
        Ok(EventResult::Consumed(None))
    }
}
