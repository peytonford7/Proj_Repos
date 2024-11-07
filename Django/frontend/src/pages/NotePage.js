import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'
//import { ReactComponent as ArrowRight } from '../assets/right.png'
import { Link } from 'react-router-dom'

const NotePage = () => {

    let{ id: noteId } = useParams();
    let [note, setNote] = useState(null);



    useEffect(() => {
        getNote()
    }, [noteId]);

    let getNote = async () => {
        let response = await fetch(`/notes/${noteId}/`)
        let data = await response.json()

        setNote(data)
    };

    return (
        <div className="note">
            <div className="note-header">
            <h3>
                <Link to="/notes">
                    <ArrowLeft />
                </Link>
            </h3>
            </div>
            <h2 className="notes-item center">
                {note?.title}
            </h2>
            <textarea defaultValue={note?.text}></textarea>
        </div>
    )
};

export default NotePage;
