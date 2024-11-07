import React, {useState, useEffect} from 'react'
import ListItem from '../components/ListItem'

const TodoListPage = () => {

    let [todos, setTodo] = useState([])

    useEffect(() => {
        getTodos()
    }, []);

    let getNotes = async () => {
        let response = await fetch('/notes')
        let data = await response.json()
        console.log('DATA: ', data)
        setNotes(data)
    };

    return (
        <div className="notes">
            <div className="notes-header">
                <h2 className="notes-title">&#9782; Notes</h2>
                <p className="notes-count">{notes.length}</p>
            </div>
            <div className="notes-list">
                {notes.map((note) => (
                    <ListItem key={note.id} note={note} />
                ))}
            </div>
        </div>
    )
};

export default NotesListPage;